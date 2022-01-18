def solve(n, diff):
    consecutive = 0
    status = diff[0]
    for i in range(n):
        if diff[i] != status:
            if diff[i] == 0:
                consecutive += 1
            status = diff[i]
    return consecutive


def main():
    with open(f"breedflip.in", "r") as fin:
        n = int(fin.readline().strip())
        a = fin.readline().strip()
        b = fin.readline().strip()
        diff = []
        for i in range(n):
            if a[i] == b[i]:
                diff.append(0)
            else:
                diff.append(1)

    with open(f"breedflip.out", "w") as fout:
        fout.write(f"{solve(n, diff)}\n")


def test():
    for k in range(1, 11):
        with open(f"breedflip_test_data/{k}.in", "r") as fin:
            n = int(fin.readline().strip())
            a = fin.readline().strip()
            b = fin.readline().strip()
            diff = []
            for i in range(n):
                if a[i] == b[i]:
                    diff.append(0)
                else:
                    diff.append(1)

        with open(f"test_outs/{k}.out", "w") as fout:
            fout.write(f"{solve(n, diff)}\n")


if __name__ == '__main__':
    test()
