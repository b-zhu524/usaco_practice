def solve(n, cows):
    res = n-1
    for i in range(n-2, -1, -1):
        if cows[i] <= cows[i+1]:
            res -= 1
        else:
            return res
    return res


def main():
    with open(f"sleepy.in", "r") as fin:
        n = int(fin.readline().strip())
        temp = fin.readline().strip().split()
        cows = [int(x) for x in temp]

    with open(f"sleepy.out", "w") as fout:
        fout.write(f"{solve(n, cows)}\n")


def test():
    for i in range(1, 13):
        with open(f"sleepy_sorting_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            temp = fin.readline().strip().split()
            cows = [int(x) for x in temp]

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, cows)}\n")


if __name__ == '__main__':
    test()
