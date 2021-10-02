from functools import cmp_to_key


def my_cmp(item1, item2):
    n1 = int(item1)
    n2 = int(item2)
    if n1 < n2:
        return -1
    elif n1 > n2:
        return 1
    else:
        return 0


l = ['1', '15', '2', '3', '23', '4']

l.sort(key=cmp_to_key(my_cmp))
print(l)
