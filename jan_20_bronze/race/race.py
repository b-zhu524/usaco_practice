def solve(n, k, x):
    s = 1
    d = 0
    t = 0

    while s < x and d <= k:
        t += 1
        d += s
        s += 1

    if d >= k:
        return t

    while k-d >= 2*s:
        t += 2
        d += 2*s
        s += 1

    while d < k:
        t += 1
        d += s
    return t


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
