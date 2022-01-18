def solve(n, k, x):
    dist = (1 + x) * x // 2
    if dist == k:
        return x

    if dist > k:
        step = x
        time = x
        while dist > k:
            dist -= step
            step -= 1
            time -= 1
        if dist < k:
            time += 1
        return time

    start_dist = (x * (x - 1)) // 2
    remaining_dist_upper = k - start_dist

    peak_upper = remaining_dist_upper - 2 * x
    peak_lower = x
    if peak_upper > peak_lower:
        peak_speed = peak_upper
        while peak_speed > peak_lower and (x + peak_speed - 1) * (peak_speed - x) > remaining_dist_upper:
            peak_speed -= 1
    else:
        peak_speed = peak_lower

    time = x - 1
    if peak_speed > x:
        l_dist = (x+peak_speed-1)*(peak_speed-x) // 2
        time += 2*(peak_speed-x)
    else:
        l_dist = 0

    remaining_dist = remaining_dist_upper - 2*l_dist
    time += remaining_dist // peak_speed
    if remaining_dist % peak_speed:
        time += 1
    return time


def main():
    with open(f"race.in", "r") as fin:
        k, n = fin.readline().strip().split()
        k, n = int(k), int(n)
        x = []
        for _ in range(n):
            temp = fin.readline().strip()
            x.append(int(temp))

    with open(f"race.out", "w") as fout:
        for i in range(n):
            fout.write(f"{solve(n, k, x[i])}\n")


def test():
    for j in range(1, 11):
        with open(f"race_test_data/{j}.in", "r") as fin:
            k, n = fin.readline().strip().split()
            k, n = int(k), int(n)
            x = []
            for _ in range(n):
                temp = fin.readline().strip()
                x.append(int(temp))

        with open(f"test_outs/{j}.out", "w") as fout:
            for i in range(n):
                fout.write(f"{solve(n, k, x[i])}\n")


if __name__ == '__main__':
    test()
