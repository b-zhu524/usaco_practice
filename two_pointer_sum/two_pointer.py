def two_pointer(a, target):
    s = 0
    e = len(a)
    while s < e:
        if s + e == target:
            return a[s], a[e]

        if s + e < target:
            s += 1
        elif s + e > target:
            e -= 1
    return -1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(two_pointer(a, 8))
