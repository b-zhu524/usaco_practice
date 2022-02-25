def repeat_num(n, k, swaps, cows):
    new_cows = cows.copy()
    cnt = 0

    while True:
        for s, e in swaps:
            while s < e:
                new_cows[s], new_cows[e] = new_cows[e], new_cows[s]
                e -= 1
                s += 1
        cnt += 1
        if cnt == k or cows == new_cows:    # k < cycle_length
            break
    return cnt, new_cows


def solve(n, k, swaps, cows):
    cycle_length, new_cows = repeat_num(n, k, swaps, cows)
    if cycle_length == k:
        return new_cows

    m = k % cycle_length
    for i in range(m):
        for s, e in swaps:
            while s < e:
                cows[s], cows[e] = cows[e], cows[s]
                e -= 1
                s += 1
    return cows


def main():
    with open(f"swap.in", "r") as fin:
        n, k = fin.readline().strip().split()
        n, k = int(n), int(k)
        swaps = []
        for j in range(2):
            s1, s2 = fin.readline().strip().split()
            swaps.append([int(s1)-1, int(s2)-1])

        cows = []
        for i in range(1, n+1):
            cows.append(i)

    res = solve(n, k, swaps, cows)
    with open(f"swap.out", "w") as fout:
        for num in res:
            fout.write(f"{num}\n")


def test():
    for j in range(1, 14):
        with open(f"swap_test_data/{j}.in", "r") as fin:
            n, k = fin.readline().strip().split()
            n, k = int(n), int(k)
            swaps = []
            for _ in range(2):
                s1, s2 = fin.readline().strip().split()
                swaps.append([int(s1) - 1, int(s2) - 1])

            cows = []
            for i in range(1, n + 1):
                cows.append(i)

        res = solve(n, k, swaps, cows)
        with open(f"test_outs/{j}.out", "w") as fout:
            for num in res:
                fout.write(f"{num}\n")


if __name__ == '__main__':
    test()
