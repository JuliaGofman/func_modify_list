def modify_list(l):
    f = list(map(lambda x: x//2, filter(lambda y: y%2==0, l)))
    l.clear()
    l.extend(f)