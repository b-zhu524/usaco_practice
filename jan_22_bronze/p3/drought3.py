def solve(n, cows):
    if n == 1:
        return 0
    if cows[0] > cows[1]:
        return -1
    if len(cows) == 2:
        if cows[1] != cows[0]:
            return -1
        return 0

    delta = [cows[i]-cows[i-1] for i in range(1, n)]
    bags = 0

    # handle d[0]
    d_val = delta[0]
    if d_val > 0:
        cows[1] -= d_val
        cows[2] -= d_val
        if cows[1] < 0 or cows[2] < 0:
            return -1
        bags += d_val * 2
        delta[0] = 0
        if len(cows) > 3:
            delta[2] += d_val

    i = 1
    # d[1] to d[len(d)-2]
    while i < n-2:
        d_val = delta[i]
        if d_val == 0:
            i += 1
            continue
        if d_val > 0:
            cows[i+1] -= d_val
            cows[i+2] -= d_val
            if cows[i+1] < 0 or cows[i+2] < 0:
                return -1
            bags += d_val * 2
            delta[i] = 0
            if i+2 < n-1:
                delta[i+2] += d_val
        else:   # < 0
            if i % 2 == 0:
                return -1
            bags += abs(d_val) * (i+1)
            if (cows[0] - abs(d_val)) < 0:
                return -1
            # for j in range(i+1):
            #     cows[j] -= abs(d_val)
            #     if cows[j] < 0:
            #         return -1
            #     bags += abs(d_val)
            delta[i] = 0
        i += 1

    # last digit of d & last 2 digits of cows
    if delta[n-2] > 0:
        return -1
    if delta[n-2] < 0:
        if (n-2) % 2 == 0:
            return -1
        bags += abs(delta[n-2]) * (n-1)
        if (cows[0] - abs(delta[n-2])) < 0:
            return -1
        # for j in range(n-1):
        #     cows[j] -= abs(delta[n-2])
        #     if cows[j] < 0:
        #         return -1
        #     bags += abs(delta[n-2])
        # delta[n-2] = 0
    return bags


def main():
    with open(f"drought.in", "r") as fin:
        t = int(fin.readline().strip())
        n_list = []
        cows_list = []
        for _ in range(t):
            n_list.append(int(fin.readline().strip()))
            temp = fin.readline().strip().split()
            cows = [int(x) for x in temp]
            cows_list.append(cows)
    with open(f"drought.out", "w") as fout:
        for i in range(t):
            fout.write(f"{solve(n_list[i], cows_list[i])}\n")


def test():
    for j in range(1, 16):
        with open(f"drought_test_data/{j}.in", "r") as fin:
            t = int(fin.readline().strip())
            n_list = []
            cows_list = []
            for _ in range(t):
                n_list.append(int(fin.readline().strip()))
                temp = fin.readline().strip().split()
                cows = [int(x) for x in temp]
                cows_list.append(cows)
        with open(f"test_outs/{j}.out", "w") as fout:
            for i in range(t):
                fout.write(f"{solve(n_list[i], cows_list[i])}\n")


if __name__ == '__main__':
    test()
