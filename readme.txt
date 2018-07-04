

parse_path(root):
    <token> (基本类型,包括枚举) . setattr(root, token, tovalue(Type, val))
    <token>:<i> (数组), value = get_or_set_attr(root, token, []), value[i] = tovalue(Type, val)
    <path1>.<path2>  (复合类型) , attr = parse_path(root, path1),  parse_path(attr, path2)


