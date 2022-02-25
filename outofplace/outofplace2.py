# works


def solve(n, cows):
    sorted_cows = sorted(cows)
    k = 0
    for i in range(n):
        if sorted_cows[i] != cows[i]:
            k += 1
    return k-1


def main():
    with open("outofplace.in", "r") as fin:
        n = int(fin.readline().strip())
        cows = []
        for _ in range(n):
            cows.append(int(fin.readline().strip()))
    with open("outofplace.out", "w") as fout:
        fout.write(f"{solve(n, cows)}\n")


def test():
    for i in range(1, 11):
        with open(f"outofplace_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            cows = []
            for _ in range(n):
                cows.append(int(fin.readline().strip()))
        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, cows)}\n")


if __name__ == '__main__':
    test()
