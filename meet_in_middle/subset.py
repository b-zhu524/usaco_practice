from math import ceil
from itertools import combinations


def generate_subsets(a):
    subset_dict = dict()
    for size in range(len(a)):
        for subset in combinations(a, size):
            if sum(subset) not in subset_dict:
                subset_dict[sum(subset)] = [subset]
            else:
                subset_dict[sum(subset)].append(subset)
    return subset_dict


def solve(a, target):
    # divide a
    a_half1 = a[:ceil(len(a)/2)]
    a_half1 = generate_subsets(a_half1)

    a_half2 = a[ceil(len(a)/2):]
    a_half2 = generate_subsets(a_half2)

    # find subsets equal to sum
    subsets = []
    for subset_sum in a_half2:
        if target - subset_sum in a_half1:
            for half1_subsets in a_half1[target-subset_sum]:
                for half2_subsets in a_half2[subset_sum]:
                    subsets.append(half1_subsets + half2_subsets)
    return subsets


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    target = 8
    print(solve(a, 8))
