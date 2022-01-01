def k_is_1(field, n):
    res = 2

    # right -> down
    h_in_top_row = "H" in field[0]
    for i in range(n):
        if field[n-1][i] == "H" or h_in_top_row:
            res -= 1
            break

    # down -> right
    h_in_bottom_row = "H" in field[n-1]
    for j in range(n):
        if field[j][0] == "H" or h_in_bottom_row:
            res -= 1
            break
    return res


def k_is_2(field, n):
    res = (n-1) * 2
    # right -> down -> right
    for i in range(n):
        h_in_bottom_row = "H" in field[n-1][i:]
        h_in_top_row = "H" in field[0][:i+1]
        if h_in_bottom_row or h_in_top_row:
            res -= 1
            if h_in_top_row:
                print("h_top", res)
            elif h_in_bottom_row:
                print("h_bottom", res)
            continue
        for j in range(1, n):
            if field[j][i] == "H":
                res -= 1
                print("h in col", res)
                break

    # down -> right -> down
    for i in range(n):
        flag = False
        for col_j in range(i+1):
            if field[0][col_j] == "H":
                res -= 1
                print("h in left_col", res)
                flag = True
                break
        if flag:
            continue

        flag = False
        for col_j in range(i+1, n):
            if field[n-1][col_j] == "H":
                res -= 1
                print("h in right_col", res)
                flag = True
                break
        if flag:
            continue

        flag = False
        for j in range(n):
            if field[i][j] == "H":
                res -= 1
                print("h in row", res)
                break
        if flag:
            continue
    return res


def k_is_3(field, n):
    res = 0
    # down -> right -> down -> right
    # right -> down -> right -> down
    return res


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
            curr_field = []
            n, turn = fin.readline().strip().split()
            n, turn = int(n), int(turn)
            ks.append(turn)
            ns.append(n)

            curr_row = []
            for i in range(n):
                curr_row.append(fin.readline().strip())
            curr_field.append(curr_row)
            fields.append(curr_row)

    print(solve(t, fields, ks, ns))


if __name__ == '__main__':
    main()
