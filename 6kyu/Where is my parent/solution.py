def find_children(dancing_brigade):
    u = [ x for x in sorted(dancing_brigade) if x.isupper() ]
    [u.insert(u.index(z.upper())+1, z) for z in [ y for y in sorted(dancing_brigade) if y.islower() ]]
    return ''.join(u)