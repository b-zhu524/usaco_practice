def linear_search(target, a):
    for i in range(len(a)):
        if a[i] == target:
            return i
    return


def binary_search(target, sorted_a):
    left_pointer = 0
    right_pointer = len(sorted_a) - 1
    mid_pointer = right_pointer + (right_pointer - left_pointer) // 2
    print(mid_pointer)
    while left_pointer != mid_pointer and right_pointer != mid_pointer:
        if sorted_a[mid_pointer] > target:
            right_pointer = mid_pointer - 1
            mid_pointer = right_pointer - left_pointer // 2
        elif sorted_a[mid_pointer] < target:
            left_pointer = mid_pointer + 1
            mid_pointer = right_pointer - left_pointer // 2
        else:
            return mid_pointer
    return -1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    out = binary_search(6, a)
    print(out)
