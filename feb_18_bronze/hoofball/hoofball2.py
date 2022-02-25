def make_graph(n, cows):
    pass_to = dict()
    in_deg = dict()

    for cow in cows:
        in_deg[cow] = 0

    pass_to[cows[0]] = cows[1]
    in_deg[cows[1]] += 1
    for i in range(1, n-1):
        rt_dist = cows[i + 1] - cows[i]
        lt_dist = cows[i] - cows[i - 1]
        if lt_dist <= rt_dist:
            pass_to[cows[i]] = cows[i - 1]
            in_deg[cows[i-1]] += 1
        else:
            pass_to[cows[i]] = cows[i + 1]
            in_deg[cows[i+1]] += 1

    pass_to[cows[-1]] = cows[-2]
    in_deg[cows[-2]] += 1
    return pass_to, in_deg


def solve(n, cow_l):
    if len(cow_l) == 2:
        return 1

    cows, in_deg = make_graph(n, cow_l)

    balls1 = 0
    balls2 = 0
    for cow in in_deg:
        if in_deg[cow] == 0:
            balls1 += 1
        elif in_deg[cow] == 1:
            a = cow
            b = cows[a]
            if in_deg[b] == 1 and cows[b] == a:
                balls2 += 1
    return balls1 + (balls2//2)


def main():
    with open(f"hoofball.in", "r") as fin:
        n = int(fin.readline().strip())
        temp = fin.readline().strip().split()
        cow_l = [int(x) for x in temp]
        cow_l.sort()

    with open(f"hoofball.out", "w") as fout:
        fout.write(f"{solve(n, cow_l)}\n")


def test():
    for i in range(1, 11):
        with open(f"hoofball_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            temp = fin.readline().strip().split()
            cow_l = [int(x) for x in temp]
            cow_l.sort()

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, cow_l)}\n")


if __name__ == '__main__':
    test()
