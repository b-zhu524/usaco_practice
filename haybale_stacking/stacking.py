def solve(n, k, instructions):
    stacks = [0 for _ in range(n)]
    marker = [0 for _ in range(n+2)]
    for i in range(k):
        i1, i2 = instructions[i][0], instructions[i][1]
        marker[i1] += 1
        marker[i2+1] -= 1

    total_sum = 0
    for i in range(n):
        total_sum += marker[i+1]
        stacks[i] = total_sum

    stacks.sort()
    return stacks[n//2]


def main():
    with open("stacking.in", "r") as fin:
        n, k = fin.readline().strip().split()
        n, k = int(n), int(k)
        instructions = []
        for _ in range(k):
            i1, i2 = fin.readline().strip().split()
            instructions.append([int(i1), int(i2)])

    with open("stacking.out", "w") as fout:
        fout.write(f"{solve(n, k, instructions)}\n")


def test():
    for i in range(1, 11):
        with open(f"stacking_test_data/{i}.in", "r") as fin:
            n, k = fin.readline().strip().split()
            n, k = int(n), int(k)
            instructions = []
            for _ in range(k):
                i1, i2 = fin.readline().strip().split()
                instructions.append([int(i1), int(i2)])

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, k, instructions)}\n")


if __name__ == "__main__":
    test()
