def k_is_1(field, n):
    res = 2

    # right -> down
    h_in_top_row = "H" in field[:n]
    for i in range(n):
        if field[i * n + (n - 1)] == "H" or h_in_top_row:
            res -= 1
            break

    # down -> right
    h_in_bottom_row = "H" in field[n*n-1-n:]
    for j in range(n):
        if field[j * n] == "H" or h_in_bottom_row:
            res -= 1
            break
    return res


def k_is_2(field, n):
    res = (n-1) * 2
    # right -> down -> right
    for i in range(n):
        h_in_bottom_row = "H" in field[i: n]
        h_in_top_row = "H" in field[:i+1]
        if h_in_bottom_row or h_in_top_row:
            res -= 1
            continue
        for j in range(1, n):
            idx = n * j + i
            if field[idx] == "H":
                res -= 1

    # down -> right -> down
    for i in range(n):
        flag = False
        for col_i in range(i+1):
            if field[n*col_i] == "H":
                res -= 1
                flag = True
                break
        if flag:
            continue

        flag = False
        for col_j in range(i+1, n):
            if field[n*col_j+n-1] == "H":
                res -= 1
                flag = True
                break
        if flag:
            continue

        for j in range(n):
            if field[i*n+j] == "H":
                res -= 1
                break
    return res


def k_is_3(field, n):
    pass


def solve(t, fields, ks, ns):
    results = []
    for i in range(t):
        if ks[i] == 1:
            results.append(k_is_1(fields[i], ns[i]))

        elif ks[i] == 2:
            results.append(k_is_2(fields[i], ns[i]))

        else:
            results.append(k_is_3(fields[i], ns[i]))
    return results


def main():
    with open("walking.in", "r") as fin:
        t = int(fin.readline().strip())
        fields = []
        ks = []
        ns = []

        for _ in range(t):
            curr_field = ""
            n, turn = fin.readline().strip().split()
            n, turn = int(n), int(turn)
            ks.append(turn)
            ns.append(n)
            for i in range(n):
                curr_field += fin.readline().strip()
            fields.append(curr_field)
    print(solve(t, fields, ks, ns))


if __name__ == '__main__':
    main()
