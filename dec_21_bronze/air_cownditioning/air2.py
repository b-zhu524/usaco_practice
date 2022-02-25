def solve(n, d):
    num_commands = 0
    i = 0
    while True:
        while i < n and d[i] == 0:
            i += 1
        if i >= n:
            break

        if d[i] > 0:
            j = i
            change = d[i]
            while j < n and d[j] > 0:
                change = min(change, d[j])
                j += 1
            num_commands += change
            for k in range(i, j):
                d[k] -= change

        else:
            j = i
            change = d[i]
            while j < n and d[j] < 0:
                change = max(change, d[j])
                j += 1
            num_commands -= change
            for k in range(i, j):
                d[k] -= change
    return num_commands


def main():
    with open("air.in", "r") as fin:
        n = int(fin.readline().strip())
        p = []
        t = []
        d = []

        for p_temp in fin.readline().strip().split():
            p.append(int(p_temp))

        for t_temp in fin.readline().strip().split():
            t.append(int(t_temp))

        for i in range(n):
            d.append(p[i] - t[i])

    with open("air.out", "w") as fout:
        fout.write(f"{solve(n, d)}\n")


def test():
    for j in range(1, 11):
        with open(f"air_cowditioning_test_data/{j}.in", "r") as fin:
            n = int(fin.readline().strip())
            p = []
            t = []
            d = []

            for p_temp in fin.readline().strip().split():
                p.append(int(p_temp))

            for t_temp in fin.readline().strip().split():
                t.append(int(t_temp))

            for i in range(n):
                d.append(p[i] - t[i])

        with open(f"test_outs/{j}.out", "w") as fout:
            fout.write(f"{solve(n, d)}\n")


if __name__ == '__main__':
    test()
