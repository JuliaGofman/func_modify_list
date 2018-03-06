def modify_list(l):
    x = []
    for i in l:
        if i % 2 == 0:
            i = i // 2
            x.append(i)
    l.clear()
    l.extend(x)