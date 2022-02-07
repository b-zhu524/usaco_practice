def find_delta(n, cows):
    delta = []
    for i in range(n-1):
        delta.append(cows[i] - cows[i+1])
    return delta


def solve(n, cows):
    d = find_delta(n, cows)
    if n == 1:
        return 0
    if n > 1 and cows[0] > cows[1]:
        return -1
    if n == 2 and cows[0] != cows[1]:
        return -1
    if n == 2 and cows[0] == cows[1]:
        return 0

    i = 0
    res = 0
    while i < n-1:
        if i < n-1 and d[i] > 0:
            res += d[i] * (i + 1)
            i += 1
        elif i < n-1 and d[i] < 0:
            res += -d[i] * (n-i)
            # j = i
            # while j < n and j != 0:
            #     j += 1
            # res += abs(d[i] * (j-i))
            i += 1
        else:
            i += 1
    return res


def is_equal(cows):
    v = cows[0]
    for c in cows:
        if cows != v:
            return False
    return True


def solve2(n, cows):
    if n == 1:
        return 0
    if n > 1 and cows[0] > cows[1]:
        return -1
    if n == 2 and cows[0] != cows[1]:
        return -1

    cnt = 0
    while True:
        for i in range(n-1):
            if is_equal(cows):
                return cnt
            cows[i] -= 1
            cows[i+1] -= 1
            cnt += 2


def main():
    t = int(input())
    cases = []
    for _ in range(t):
        n = int(input())
        temp = input().strip().split()
        cows = [int(x) for x in temp]
        cases.append([n, cows])
    for i in range(t):
        curr_n, curr_cows = cases[i]
        print(f"{solve(curr_n, curr_cows)}")


if __name__ == '__main__':
    main()
