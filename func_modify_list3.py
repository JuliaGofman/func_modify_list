def modify_list(l):
    l[:] = [a//2 for a in l if a%2 == 0]
lst = [2, 3, 4, 5, 6, 7, 8]
modify_list(lst)
print(lst)