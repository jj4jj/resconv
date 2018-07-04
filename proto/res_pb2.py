# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: res.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='res.proto',
  package='ux',
  serialized_pb=_b('\n\tres.proto\x12\x02ux\"7\n\x04\x41Msg\x12\x15\n\x02\x65t\x18\x01 \x01(\x0e\x32\t.ux.EType\x12\x0b\n\x03i32\x18\x02 \x01(\x05\x12\x0b\n\x03str\x18\x03 \x01(\t\"N\n\x04\x42Msg\x12\x15\n\x02\x65t\x18\x01 \x01(\x0e\x32\t.ux.EType\x12\x0b\n\x03i32\x18\x02 \x01(\x05\x12\x0b\n\x03str\x18\x03 \x01(\t\x12\x15\n\x03\x61mf\x18\x04 \x01(\x0b\x32\x08.ux.AMsg\"u\n\x08TestDesc\x12\x0b\n\x03i32\x18\x01 \x01(\x05\x12\n\n\x02\x64\x66\x18\x02 \x01(\x01\x12\n\n\x02\x62\x66\x18\x03 \x01(\x08\x12\x15\n\x03\x61mf\x18\x04 \x01(\x0b\x32\x08.ux.AMsg\x12\x15\n\x03\x62mf\x18\x05 \x01(\x0b\x32\x08.ux.BMsg\x12\x16\n\x04ramf\x18\x06 \x03(\x0b\x32\x08.ux.AMsg\"(\n\nTBTestDesc\x12\x1a\n\x04list\x18\x01 \x03(\x0b\x32\x0c.ux.TestDesc*(\n\x05\x45Type\x12\x0b\n\x07\x45T_NONE\x10\x00\x12\x08\n\x04\x45T_A\x10\x01\x12\x08\n\x04\x45T_B\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ETYPE = _descriptor.EnumDescriptor(
  name='EType',
  full_name='ux.EType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ET_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ET_A', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ET_B', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=315,
  serialized_end=355,
)
_sym_db.RegisterEnumDescriptor(_ETYPE)

EType = enum_type_wrapper.EnumTypeWrapper(_ETYPE)
ET_NONE = 0
ET_A = 1
ET_B = 2



_AMSG = _descriptor.Descriptor(
  name='AMsg',
  full_name='ux.AMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='et', full_name='ux.AMsg.et', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i32', full_name='ux.AMsg.i32', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str', full_name='ux.AMsg.str', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=72,
)


_BMSG = _descriptor.Descriptor(
  name='BMsg',
  full_name='ux.BMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='et', full_name='ux.BMsg.et', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i32', full_name='ux.BMsg.i32', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str', full_name='ux.BMsg.str', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amf', full_name='ux.BMsg.amf', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=152,
)


_TESTDESC = _descriptor.Descriptor(
  name='TestDesc',
  full_name='ux.TestDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='i32', full_name='ux.TestDesc.i32', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='df', full_name='ux.TestDesc.df', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bf', full_name='ux.TestDesc.bf', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amf', full_name='ux.TestDesc.amf', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bmf', full_name='ux.TestDesc.bmf', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ramf', full_name='ux.TestDesc.ramf', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=271,
)


_TBTESTDESC = _descriptor.Descriptor(
  name='TBTestDesc',
  full_name='ux.TBTestDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='ux.TBTestDesc.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=313,
)

_AMSG.fields_by_name['et'].enum_type = _ETYPE
_BMSG.fields_by_name['et'].enum_type = _ETYPE
_BMSG.fields_by_name['amf'].message_type = _AMSG
_TESTDESC.fields_by_name['amf'].message_type = _AMSG
_TESTDESC.fields_by_name['bmf'].message_type = _BMSG
_TESTDESC.fields_by_name['ramf'].message_type = _AMSG
_TBTESTDESC.fields_by_name['list'].message_type = _TESTDESC
DESCRIPTOR.message_types_by_name['AMsg'] = _AMSG
DESCRIPTOR.message_types_by_name['BMsg'] = _BMSG
DESCRIPTOR.message_types_by_name['TestDesc'] = _TESTDESC
DESCRIPTOR.message_types_by_name['TBTestDesc'] = _TBTESTDESC
DESCRIPTOR.enum_types_by_name['EType'] = _ETYPE

AMsg = _reflection.GeneratedProtocolMessageType('AMsg', (_message.Message,), dict(
  DESCRIPTOR = _AMSG,
  __module__ = 'res_pb2'
  # @@protoc_insertion_point(class_scope:ux.AMsg)
  ))
_sym_db.RegisterMessage(AMsg)

BMsg = _reflection.GeneratedProtocolMessageType('BMsg', (_message.Message,), dict(
  DESCRIPTOR = _BMSG,
  __module__ = 'res_pb2'
  # @@protoc_insertion_point(class_scope:ux.BMsg)
  ))
_sym_db.RegisterMessage(BMsg)

TestDesc = _reflection.GeneratedProtocolMessageType('TestDesc', (_message.Message,), dict(
  DESCRIPTOR = _TESTDESC,
  __module__ = 'res_pb2'
  # @@protoc_insertion_point(class_scope:ux.TestDesc)
  ))
_sym_db.RegisterMessage(TestDesc)

TBTestDesc = _reflection.GeneratedProtocolMessageType('TBTestDesc', (_message.Message,), dict(
  DESCRIPTOR = _TBTESTDESC,
  __module__ = 'res_pb2'
  # @@protoc_insertion_point(class_scope:ux.TBTestDesc)
  ))
_sym_db.RegisterMessage(TBTestDesc)


# @@protoc_insertion_point(module_scope)
