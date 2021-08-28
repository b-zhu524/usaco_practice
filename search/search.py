def linear_search(target, a):
    for i in range(len(a)):
        if a[i] == target:
            return i
    return -1


def linear_search_max(a):
    max_val = a[0]
    max_idx = 0
    for i in range(1, len(a)):
        if a[i] > max_val:
            max_val = a[i]
            max_idx = i
    return max_val, max_idx


def linear_search_avg(a):
    sum_val = 0
    for i in range(len(a)):
        sum_val += a[i]
    return sum_val / len(a)


def linear_search_product(a):
    mul_val = 1
    for i in range(len(a)):
        mul_val *= a[i]
    return mul_val


def binary_search(target, sorted_a):
    left_pointer = 0
    right_pointer = len(sorted_a) - 1

    while left_pointer <= right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2

        if sorted_a[mid_pointer] == target:
            return mid_pointer
        elif sorted_a[mid_pointer] < target:
            left_pointer = mid_pointer + 1
        elif sorted_a[mid_pointer] > target:
            right_pointer = mid_pointer - 1
    return -1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    out = binary_search(10, a)
    print(out)
