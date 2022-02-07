def solve(n, swaps):
    shells = [1, 0, 0]

    score1 = 0
    for a, b, g in swaps:
        shells[a], shells[b] = shells[b], shells[a]
        if shells[g] == 1:
            score1 += 1

    score2 = 0
    shells = [0, 1, 0]
    for a, b, g in swaps:
        shells[a], shells[b] = shells[b], shells[a]
        if shells[g] == 1:
            score2 += 1

    score3 = 0
    shells = [0, 0, 1]
    for a, b, g in swaps:
        shells[a], shells[b] = shells[b], shells[a]
        if shells[g] == 1:
            score3 += 1
    return max(score1, score2, score3)


def main():
    with open(f"shell.in", "r") as fin:
        n = int(fin.readline().strip())
        swaps = []
        for _ in range(n):
            a, b, g = fin.readline().strip().split()
            swaps.append((int(a)-1, int(b)-1, int(g)-1))
    with open(f"shell.out", "w") as fout:
        fout.write(f"{solve(n, swaps)}\n")


def test():
    for i in range(1, 11):
        with open(f"shell_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            swaps = []
            for _ in range(n):
                a, b, g = fin.readline().strip().split()
                swaps.append((int(a) - 1, int(b) - 1, int(g) - 1))
        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, swaps)}\n")


if __name__ == '__main__':
    test()
