def mark(n, p, t):
    decreasing = []
    increasing = []

    curr_inc = []
    curr_dec = []
    min_curr_inc = None
    min_curr_dec = None

    for i in range(n):
        if len(curr_inc) == 2:
            curr_inc.append(min_curr_inc)
            curr_inc.append(i)
            increasing.append(curr_inc)
            curr_inc = []
            min_curr_inc = None

        if len(curr_dec) == 2:
            curr_dec.append(min_curr_dec)
            curr_dec.append(i)
            decreasing.append(curr_dec)
            curr_dec = []
            min_curr_dec = None

        if p[i] == t[i]:
            continue

        # decreasing
        if t[i] > p[i] and len(curr_dec) == 0:
            if len(curr_inc) == 1:
                curr_inc.append(i)
            if min_curr_dec is None or t[i] - p[i] < min_curr_dec:
                min_curr_dec = t[i] - p[i]
            curr_dec.append(i)

        # increasing
        if t[i] < p[i] and len(curr_inc) == 0:
            if len(curr_dec) == 1:
                print(curr_dec)
                curr_dec.append(i)
            if min_curr_dec is None or p[i] - t[i] < min_curr_inc:
                min_curr_inc = p[i] - t[i]
            curr_inc.append(i)

    return decreasing, increasing


def solve(n, p, t):
    res = 0
    decreasing, increasing = mark(n, p, t)

    print(decreasing, increasing)
    return res


def main():
    with open("air.in", "r") as fin:
        n = int(fin.readline().strip())
        p = []
        t = []

        for p_i in fin.readline().strip().split():
            p.append(int(p_i))

        for t_i in fin.readline().strip().split():
            t.append(int(t_i))

    with open("air.out", "w") as fout:
        print(solve(n, p, t))


if __name__ == '__main__':
    main()
