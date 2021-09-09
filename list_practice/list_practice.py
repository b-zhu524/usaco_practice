def reversed_list(a, start_idx, end_idx):
    while end_idx > start_idx:
        a[start_idx], a[end_idx] = a[end_idx], a[start_idx]
        start_idx += 1
        end_idx -= 1
    return a


def largest_sublist(a):
    largest_sum = None
    best_start, best_end = 0, 0
    for i in range(len(a)):
        sum_sublist = 0
        for j in range(i, len(a)):
            sum_sublist += a[j]
            if largest_sum is None or sum_sublist > largest_sum:
                largest_sum = sum_sublist
                best_start = i
                best_end = j
    return best_start, best_end, largest_sum


def faster_largest_sublist(a):
    current_best_start = 0
    current_best_sum = a[0]

    t_best_sum = current_best_sum
    t_best_start = current_best_start
    t_best_end = 0

    for i in range(1, len(a)):
        if current_best_sum < 0:
            current_best_sum = a[i]
            current_best_start = i
        else:
            current_best_sum += a[i]

        if t_best_sum < current_best_sum:
            t_best_sum = current_best_sum
            t_best_start = current_best_start
            t_best_end = i
    return t_best_start, t_best_end, t_best_sum


def test_reverse_list():
    a = [0, 1, -2, 3, 4, -100, 5, 6, -1, 7, 8, 9]
    out = largest_sublist(a)
    out2 = faster_largest_sublist(a)
    print(out, out2)


if __name__ == "__main__":
    test_reverse_list()
