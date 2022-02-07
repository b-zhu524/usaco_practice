def solve(g, a, g_cnt, a_cnt):
    green = 0
    for i in range(3):
        for j in range(3):
            if g[i][j] == a[i][j]:
                g_cnt[g[i][j]] -= 1
                a_cnt[g[i][j]] -= 1
                green += 1

    x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
    yellow = 0
    for char in x:
        yellow += min(g_cnt[char], a_cnt[char])
    return green, yellow


def main():
    g = []
    a = []
    g_cnt = dict()
    a_cnt = dict()
    for _ in range(3):
        g.append(input().strip())
    for _ in range(3):
        a.append(input().strip())

    x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
    for char in x:
        a_cnt[char] = 0
        g_cnt[char] = 0
    for i in range(3):
        for j in range(3):
            g_cnt[g[i][j]] += 1
            a_cnt[a[i][j]] += 1

    g, y = solve(g, a, g_cnt, a_cnt)
    print(f"{g}")
    print(f"{y}")


if __name__ == '__main__':
    main()
