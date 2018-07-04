#coding:utf-8
from __future__ import unicode_literals
import os
import sys
import xlrd
import logging
from google.protobuf.text_format import MessageToString

enum_cn_map = {}
res = None
"""
CPPTYPE_INT32       = 1,     // TYPE_INT32, TYPE_SINT32, TYPE_SFIXED32
CPPTYPE_INT64       = 2,     // TYPE_INT64, TYPE_SINT64, TYPE_SFIXED64
CPPTYPE_UINT32      = 3,     // TYPE_UINT32, TYPE_FIXED32
CPPTYPE_UINT64      = 4,     // TYPE_UINT64, TYPE_FIXED64
CPPTYPE_DOUBLE      = 5,     // TYPE_DOUBLE
CPPTYPE_FLOAT       = 6,     // TYPE_FLOAT
CPPTYPE_BOOL        = 7,     // TYPE_BOOL
CPPTYPE_ENUM        = 8,     // TYPE_ENUM
CPPTYPE_STRING      = 9,     // TYPE_STRING, TYPE_BYTES
CPPTYPE_MESSAGE     = 10,    // TYPE_MESSAGE, TYPE_GROUP
MAX_CPPTYPE         = 10,    // Constant useful for defining lookup tables
// indexed by CppType.
"""

def check_str_number(s):
    try:
        return True,float(s)
    except ValueError:
        return False,0

def field_value_from_str(field, val):
    field_type = field.cpp_type
    if field_type >= 5 and field_type <= 6:
        return float(val)
    if field_type in (1,3):
        return int(float(val))
    if field_type in (2,4):
        return long(float(val))
    if field_type == 9:
        return val
    if field_type == 7:
        if val.lower() in ('true','1','yes'):
            return True
        else:
            return False
    if field_type == 8:
        evd = None
        isn, fval=check_str_number(val)
        if isn:
            evd=field.enum_type.values_by_number[int(fval)]
        if val in field.enum_type.values_by_name:
            evd=field.enum_type.values_by_name[val]
        #todo get by map
        enval = 0
        if evd is None and field.enum_type.name in enum_cn_map:
            cn_map = enum_cn_map[field.enum_type.name]
            if val in cn_map:
                enval = cn_map[val]
            else:
                raise Exception("error enum value:'%s'" % val)
        else:
            enval = evd.number
        return enval

    if field_type == 10:
        return None

def field_default_value(field):
    field_type = field.cpp_type
    if field_type >= 1 and field_type <= 6:
        return 0
    if field_type == 7:
        return False
    if field_type == 8:
        return field.default_value
    if field_type == 9:
        return ""
    return None


def object_mutable_touch(obj, token, val=None):
    ks = token.split(':')
    if ks[0] not in obj.DESCRIPTOR.fields_by_name:
        logging.error("excel error column:%s not exist in res def", token)
        return None
    field = obj.DESCRIPTOR.fields_by_name[ks[0]]
    assert len(ks) <= 2 and len(ks) > 0, "error path fromat array must be (name:index)"
    pval = field_value_from_str(field, val)
    dval = field_default_value(field)
    attr = getattr(obj, ks[0])
    if len(ks) == 1:
        if field.cpp_type == 10:
            return attr
        else:
            setattr(obj, token, pval)
    else:
        idx = int(ks[1])
        assert idx<64,"array index range is from 0 to 64"
        if len(attr) <= idx:
            for x in range(idx - len(attr) - 1):
                if field.cpp_type == 10:
                    attr.add()
                else:
                    attr.append(dval)
            ######################## current#############
            if field.cpp_type == 10:
                return attr.add()
            else:
                attr.append(pval)
        else:
            if field.cpp_type == 10:
                return attr[idx] 
            else:
                attr[idx] = pval
        

def object_parse_from_path(obj, path, val):
    np = path.find('.')
    if np != -1:
        token = path[:np]
        attr = object_mutable_touch(obj, token)
        assert attr is not None,"touch path:%s val:%s maybe not match attr is None" % (path, val)
        object_parse_from_path(attr, path[np+1:], val)
    else:
        attr = object_mutable_touch(obj, path, val)


def object_parse_from_row(obj, kvs):
    for k,v in kvs.items():
        object_parse_from_path(obj, k, unicode(v))

def datasets_parse_from_xlsx(path):
    workbook = xlrd.open_workbook(path)
    datasets = []
    for sn in workbook.sheet_names():
        if sn.startswith('_'):
            logging.debug("skip sheet name:%s", sn)
            continue
        sheet = workbook.sheet_by_name(sn)
        #row:(1,2) => meta
        if sheet.nrows <= 2:
            logging.debug("skip sheet name:%s for rows less than 2", sn)
            continue
        meta_row = sheet.row_values(1)
        for nr in xrange(sheet.nrows - 2):
            row = sheet.row_values(2+nr)
            data = {}
            ith = 0
            for k in meta_row:
                data[k] = row[ith] 
                ith = ith + 1
            datasets.append(data)
    return datasets


def read_table_from_xlsx(TBTypeName,path):
    global res
    TBMeta = getattr(res, TBTypeName)
    tb=TBMeta()
    datasets = datasets_parse_from_xlsx(path)
    for data in datasets:
        row_obj = tb.list.add()
        object_parse_from_row(row_obj, data)
    return tb


def convert(path, dstdir):
    name = os.path.basename(path)
    TBTypeName = name.split('_')[0]
    tb = read_table_from_xlsx(TBTypeName, path)
    buff = tb.SerializeToString()
    pbinf = '%s/%s.pbin' % (dstdir, TBTypeName)
    open(pbinf,"w").write(buff)
    ptxtf = '%s/%s.txt' % (dstdir, TBTypeName)
    open(ptxtf,"w").write(MessageToString(tb))
    logging.debug("convert pbin path:%s -> %s,%s ...", path, pbinf, ptxtf)

def pbin_dump(path):
    name = os.path.basename(path)
    TBTypeName = name.split('.')[0]
    tb = getattr(res, TBTypeName)()
    buff = open(path,"r").read()
    tb.ParseFromString(buff)
    print(MessageToString(tb))


def main():
    run_mode = 0 #convert
    if '--dump' in sys.argv:
        run_mode = 1
        sys.argv.remove('--dump')
    elif '--convert' in sys.argv:
        sys.argv.remove('--convert')
    global res 
    protopath= './proto/res_pb2'
    if run_mode == 0 and len(sys.argv) > 2:
        logging.basicConfig(level=logging.DEBUG)
        srcdir=sys.argv[1]
        paths=sys.argv[2]
        dstdir = '.'
        if(len(sys.argv)>3):
            dstdir=sys.argv[3]
        if(len(sys.argv)>4):
            protopath=sys.argv[4]
        proto_dir=os.path.dirname(protopath)
        proto_py=os.path.basename(protopath)
        sys.path.append(proto_dir)
        res = __import__(proto_py)
        [convert(srcdir+'/'+path, dstdir) for path in paths.split(',')]
    elif run_mode == 1 and len(sys.argv) > 1:
        if len(sys.argv) > 2:
            protopath=sys.argv[2]
        proto_dir=os.path.dirname(protopath)
        proto_py=os.path.basename(protopath)
        sys.path.append(proto_dir)
        res = __import__(proto_py)
        pbin_dump(sys.argv[1])
    else:
        print('Usage: python %s <xlsx dir> <xlsx file list> [output dir] [proto path] [--convert]' % sys.argv[0])
        print('     : python %s <pbin path> [proto path] --dump' % sys.argv[0])
        print('\tExample:python %s ./xlsx TBTestDesc_test.xlsx ./res ./proto/res_pb2' % sys.argv[0])
        print('\tExample:python %s ./res/TBTestDesc.pbin ./proto/res_pb2 --dump #dump the pbin with string' % sys.argv[0])
        print("")


if __name__ == '__main__':
    main()
