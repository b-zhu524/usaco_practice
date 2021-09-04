def find_fitting_stalls(cow_height, sorted_stalls):
    acc = 0
    for i in range(len(sorted_stalls)):
        if sorted_stalls[i] >= cow_height:
            acc += 1
        else:
            break
    return acc


def solve(cows, stalls):
    permutations = 1
    cows.sort(reverse=True)
    stalls.sort(reverse=True)
    for i in range(len(cows)):
        permutations *= find_fitting_stalls(cows[i], stalls) - i
    return permutations


def main():
    _ = int(input())
    cows = [int(cow) for cow in input().split()]
    stalls = [int(stall) for stall in input().split()]
    print(solve(cows, stalls))


def test():
    for i in range(1, 13):
        with open(f"just_stalling_test_data/{i}.in", "r") as fin:
            _ = int(fin.readline().strip())
            cows = [int(cow) for cow in fin.readline().strip().split()]
            stalls = [int(stall) for stall in fin.readline().strip().split()]

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(cows, stalls)}\n")


if __name__ == "__main__":
    test()
