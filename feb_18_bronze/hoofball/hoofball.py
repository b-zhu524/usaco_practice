def furthest_0_from_right(n, marker):
    for i in range(n-1, -1, -1):
        if marker[i] == 0:
            return i
    return -1


def nearest(closest, m):
    d1 = -1
    d2 = -1
    if closest != 0 and m[closest] - m[closest - 1]:
        d1 = m[closest] - m[closest - 1]
    else:
        d2 = m[closest + 1] - m[closest]

    return d1, d2


def all_dist(n, cows):
    dists = []
    for i in range(n-1):
        dists.append(cows[i+1]-cows[i])
    return dists


def throw(n, cows, dist, i):
    if i < n-2 and dist[i] > dist[i+1]:
        return i + 1
    return i - 1


def solve(n, cows):
    cows.sort()
    m = [0 for _ in range(n)]
    dist = all_dist(n, cows)
    zero_cnt = n-1
    num_balls = 1

    closest = 0
    while True:
        if zero_cnt == 0:
            break
        for _ in range(n):
            mark = throw(n, cows, dist, closest)
            if m[mark] == 0:
                zero_cnt -= 1
            closest = mark
            m[mark] += 1
        closest = furthest_0_from_right(n, m)
        num_balls += 1

    return num_balls


def main():
    with open(f"hoofball.in", "r") as fin:
        n = int(fin.readline().strip())
        temp = fin.readline().strip().split()
        cows = [int(x) for x in temp]

    with open(f"hoofball.out", "w") as fout:
        fout.write(f"{solve(n, cows)}\n")


def test():
    for i in range(1, 11):
        with open(f"hoofball_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            temp = fin.readline().strip().split()
            cows = [int(x) for x in temp]

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, cows)}\n")


if __name__ == '__main__':
    main()
