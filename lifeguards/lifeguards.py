<<<<<<< HEAD
def solve():
    pass


def main():
    pass


def intersection(interval1, interval2):
    return max(0, min(interval2) - max(interval1))


if __name__ == '__main__':
    main()
=======
def fire(shifts, fire_idx):
    new_shifts = shifts[:]
    new_shifts[fire_idx] = None
    return new_shifts


def intersection(line1, line2):
    intersect = max(0, line2[0]-line1[1])
    return intersect


def total_time(shifts):
    interval_sum = 0
    intersection_sum = 0
    for i in range(len(shifts)-1):
        if shifts[i] is None:
            continue

        if shifts[i+1] is not None and i < len(shifts):
            curr_intersect = intersection(shifts[i], shifts[i+1])
            intersection_sum += curr_intersect

        interval_sum += (shifts[i][1] - shifts[i][0])

    return interval_sum - intersection_sum


def solve(n, shifts):
    max_time = None
    for i in range(n):
        new_shifts = fire(shifts, i)
        new_time = total_time(new_shifts)

        if max_time is None or new_time > max_time:
            max_time = new_time
    return max_time


def main():
    with open("lifeguards.in", "r") as fin:
        n = int(fin.readline().strip())
        shifts = []
        for _ in range(n):
            start_t, end_t = fin.readline().strip().split()
            start_t, end_t = int(start_t), int(end_t)
            shifts.append((start_t, end_t))

    res = solve(n, shifts)
    with open("lifeguards.out", "w") as fout:
        fout.write(f"{res}\n")


def test():
    for i in range(1, 11):
        with open(f"lifeguards_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            shifts = []
            for _ in range(n):
                start_t, end_t = fin.readline().strip().split()
                start_t, end_t = int(start_t), int(end_t)
                shifts.append((start_t, end_t))

        res = solve(n, shifts)
        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{res}\n")


if __name__ == '__main__':
    test()
>>>>>>> origin/master
