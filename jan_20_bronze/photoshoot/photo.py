def solve(n, b):
    good_cows = set(range(1, n+1))
    for start in range(1, n):
        curr_sol = [start]
        seen = set()
        seen.add(start)

        flag = False
        for i in range(1, n):
            ai = b[i-1] - curr_sol[i-1]
            if ai not in good_cows or ai in seen:
                flag = True
                break
            seen.add(ai)
            curr_sol.append(ai)
        if flag:
            continue
        return curr_sol
    return -1


def main():
    with open("photo.in", "r") as fin:
        n = int(fin.readline().strip())
        temp = fin.readline().strip().split()
        b = [int(x) for x in temp]

    res = solve(n, b)
    with open("photo.out", "w") as fout:
        for i in range(len(res)):
            fout.write(f"{res[i]}")
            if i != len(res)-1:
                fout.write(" ")
        fout.write("\n")


def test():
    for j in range(1, 11):
        with open(f"photoshoot_test_data/{j}.in", "r") as fin:
            n = int(fin.readline().strip())
            temp = fin.readline().strip().split()
            b = [int(x) for x in temp]

        res = solve(n, b)
        with open(f"test_outs/{j}.out", "w") as fout:
            for i in range(len(res)):
                fout.write(f"{res[i]}")
                if i != len(res) - 1:
                    fout.write(" ")
            fout.write("\n")


if __name__ == '__main__':
    test()
