def solve(d, n):
    commands = 0

    i = 0
    while True:
        while i < n and d[i] == 0:
            i += 1
        if i >= n:
            break

        elif d[i] > 0:
            j = i
            small = d[i]
            while j < n and d[j] > 0:
                small = min(small, d[j])
                j += 1
            commands += small
            for k in range(i, j):
                d[k] -= small

        else:
            j = i
            large = d[i]
            while j < n and d[j] < 0:
                large = max(large, d[j])
                j += 1
            commands += large
            for k in range(i, j):
                d[k] -= large
    return commands


def main():
    with open("air.in", "r") as fin:
        n = int(fin.readline().strip())
        p = []
        t = []
        d = []
        for num in fin.readline().strip().split():
            p.append(int(num))
        for num in fin.readline().strip().split():
            t.append(int(num))
        d = [p[i]-t[i] for i in range(n)]
    with open("air.out", "w") as fout:
        fout.write(f"{solve(d, n)}\n")


def test():
    for j in range(1, 11):
        with open(f"aircowditioning_test_data/{j}.out", "r") as fin:
            n = int(fin.readline().strip())
            p = []
            t = []
            d = []
            for num in fin.readline().strip().split():
                p.append(int(num))
            for num in fin.readline().strip().split():
                t.append(int(num))
            d = [p[i] - t[i] for i in range(n)]
        with open(f"test_outs/{j}.out", "w") as fout:
            fout.write(f"{solve(d, n)}\n")


if __name__ == '__main__':
    test()
