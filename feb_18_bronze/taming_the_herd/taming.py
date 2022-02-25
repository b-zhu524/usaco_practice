def solve(n, b):
    if b[0] > 0:
        return -1

    b[0] = 0
    for i in range(n-1, -1, -1):
        if i < n-1 and b[i+1] > 0:
            if b[i] == -1:
                b[i] = b[i+1] - 1
    for i in range(n-1):
        if b[i] > -1 and b[i+1] > 0:
            if b[i] + 1 != b[i+1]:
                return -1

    neg_1_cnt = 0
    zero_cnt = 0
    for log in b:
        if log == -1:
            neg_1_cnt += 1
        elif log == 0:
            zero_cnt += 1

    return zero_cnt, zero_cnt + neg_1_cnt


def main():
    with open(f"taming.in", "r") as fin:
        n = int(fin.readline().strip())
        temp = fin.readline().strip().split()
        breakouts = [int(x) for x in temp]

    res = solve(n, breakouts)
    with open(f"taming.out", "w") as fout:
        if res == -1:
            fout.write(f"{res}\n")
        else:
            fout.write(f"{res[0]} {res[1]}\n")


def test():
    for i in range(1, 11):
        with open(f"taming_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            temp = fin.readline().strip().split()
            breakouts = [int(x) for x in temp]

        res = solve(n, breakouts)
        with open(f"test_outs/{i}.out", "w") as fout:
            if res == -1:
                fout.write(f"{res}\n")
            else:
                fout.write(f"{res[0]} {res[1]}\n")


if __name__ == '__main__':
    test()
