from itertools import combinations


def has_carries(n1, n2):
    while n1 != 0 and n2 != 0:
        if n1 % 10 + n2 % 10 > 9:
            return True
        n1 = n1 // 10
        n2 = n2 // 10
    return False


def has_carries_all(subset):
    total_sum = 0
    for i in range(len(subset)):
        if has_carries(total_sum, subset[i]):
            return True
        else:
            total_sum += subset[i]
    return False


def solve(N, weights):
    for size in range(N, 1, -1):
        for c in combinations(weights, size):
            if not has_carries_all(c):
                return size
    return 1


def main():
    with open("escape.in", "r") as fin:
        N = int(fin.readline().strip())
        weights = []
        for i in range(N):
            weight = int(fin.readline().strip())
            weights.append(weight)
    with open("escape.out", "w") as fout:
        fout.write(f"{solve(N, weights)}\n")


if __name__ == "__main__":
    main()
