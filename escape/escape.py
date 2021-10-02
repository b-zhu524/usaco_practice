from itertools import combinations
from functools import cmp_to_key

# def check_all_carries(indices, weights):
#     total_sum = 0
#     for idx in indices:
#         weight = weights[idx]
#         if has_carries(total_sum, weight):
#             return True
#         total_sum += weight
#     return False


# def solve(N, weights):
#     for size in range(N, 0, -1):
#         for indices in combinations(range(N), size):
#             if not check_all_carries(indices, weights):
#                 return size

def has_carries(num1, num2):
    while num1 != 0 or num2 != 0:
        if num1 % 10 + num2 % 10 >= 10:
            return True
        num1 = num1 // 10
        num2 = num2 // 10
    return False


def check_all_carries(weights):
    total_sum = 0
    for weight in weights:
        if has_carries(total_sum, weight):
            return True
        total_sum += weight
    return False


def solve(N, weights):
    for size in range(N, 0, -1):
        for subset in combinations(weights, size):
            if not check_all_carries(subset):
                return size


# def solve(N, weights):
#     result = 0
#     for number in range(1, 1 << N):
#         subset = []
#         for n in range(N):
#             if number & (1 << n) != 0:
#                 subset.append(weights[n])
#         if not check_all_carries(subset) and len(subset) > result:
#             result = len(subset)
#     return result


def main():
    with open("escape.in", "r") as fin:
        N = int(fin.readline().strip())
        weights = []
        for i in range(N):
            weight = int(fin.readline().strip())
            weights.append(weight)

    with open("escape.out", "w") as fout:
        fout.write(f"{solve(N, weights)}\n")


def test():
    for j in range(1, 11):
        with open(f"escape_farm_test_data/I.{j}", "r") as fin:
            N = int(fin.readline().strip())
            weights = []
            for i in range(N):
                weight = int(fin.readline().strip())
                weights.append(weight)

        with open(f"test_outs/O.{j}", "w") as fout:
            fout.write(f"{solve(N, weights)}\n")


if __name__ == "__main__":
    main()
    test()
