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

    min_num = 1000000001

    # find even xs
    x2 = delta[0]
    bags += x2 * 2
    cows[1] -= x2
    cows[2] -= x2
    if x2 < 0 or cows[1] < 0 or cows[2] < 0:
        return -1
    min_num = min(min_num, cows[1], cows[2])
    prev_x = x2
    i = 0
    while i < len(delta):
        i += 2
        if i >= len(delta) - 1:
            break

        new_x = delta[i] + prev_x
        cows[i+1] -= new_x
        cows[i+2] -= new_x
        if new_x < 0 or cows[i+1] < 0 or cows[i+2] < 0:
            return -1
        min_num = min(min_num, cows[i+1], cows[i+2])
        bags += new_x * 2
        prev_x = new_x

    # odd numbers
    x1 = cows[0] - min_num
    i = -1
    cows[i+1] -= x1
    cows[i+2] -= x1
    if x1 < 0 or cows[i+1] < 0 or cows[i+2] < 0:
        return -1
    bags += x1 * 2
    prev_x = x1
    while i < len(delta):
        i += 2
        if i >= len(delta) - 1:
            break
        new_x = delta[i] + prev_x
        cows[i + 1] -= new_x
        cows[i + 2] -= new_x
        if new_x < 0 or cows[i + 1] < 0 or cows[i + 2] < 0:
            return -1
        bags += new_x * 2
        prev_x = new_x
    return bags


def main():
    with open(f"drought.in", "r") as fin:
        t = int(fin.readline().strip())
        n_list = []
        cows_list = []
        for _ in range(t):
            n_list.append(int(fin.readline().strip()))
            cows = fin.readline().strip().split()
            cows = [int(x) for x in cows]
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
                cows = fin.readline().strip().split()
                cows = [int(x) for x in cows]
                cows_list.append(cows)
        with open(f"test_outs/{j}.out", "w") as fout:
            for i in range(t):
                fout.write(f"{solve(n_list[i], cows_list[i])}\n")


if __name__ == '__main__':
    test()
