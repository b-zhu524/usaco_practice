def num_paths(field, k, n):
    res = 0
    if k >= 1:
        dr = True
        rd = True
        for i in range(1, n):
            if field[0][i] == "H" or field[i][n-1] == "H":
                rd = False

            if field[i][0] == "H" or field[n-1][i] == "H":
                dr = False

        if dr:
            res += 1
        if rd:
            res += 1

    if k >= 2:
        for t in range(1, n-1):
            rdr = True
            drd = True
            for i in range(1, t+1):
                if field[0][i] == "H":
                    rdr = False
                if field[i][0] == "H":
                    drd = False

            for i in range(n):
                if field[i][t] == "H":
                    rdr = False
                if field[t][i] == "H":
                    drd = False

            for i in range(t+1, n):
                if field[n-1][i] == "H":
                    rdr = False
                if field[i][n-1] == "H":
                    drd = False

            if rdr:
                res += 1
            if drd:
                res += 1

    if k == 3:
        for t1 in range(1, n-1):
            for t2 in range(1, n-1):
                rdrd = True
                drdr = True
                for i in range(1, t1+1):
                    if field[0][i] == "H":
                        rdrd = False
                    if field[i][0] == "H":
                        drdr = False

                for i in range(0, t2+1):
                    if field[i][t1] == "H":
                        rdrd = False
                    if field[t1][i] == "H":
                        drdr = False
                for i in range(t1+1, n):
                    if field[t2][i] == "H":
                        rdrd = False
                    if field[i][t2] == "H":
                        drdr = False
                for i in range(t2+1, n):
                    if field[i][n-1] == "H":
                        rdrd = False
                    if field[n-1][i] == "H":
                        drdr = False

                if rdrd:
                    res += 1
                if drdr:
                    res += 1
    return res


def solve(t, fields, ks, ns):
    results = []
    for i in range(t):
        field = fields[i]
        results.append(num_paths(field, ks[i], ns[i]))
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

    with open(f"walking.out", "w") as fout:
        fout.write(f"{solve(t, fields, ks, ns)}\n")


def test():
    for j in range(1, 11):
        with open(f"walking_home_test_data/{j}.in", "r") as fin:
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

        res = solve(t, fields, ks, ns)
        with open(f"test_outs/{j}.out", "w") as fout:
            for num in res:
                fout.write(f"{num}\n")


if __name__ == '__main__':
    test()
