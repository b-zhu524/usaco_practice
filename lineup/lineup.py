from itertools import permutations


def solve(constraints):
    cows = ["Bessie", "Buttercup", "Belinda", "Beatrice",
            "Bella", "Blue", "Betsy", "Sue"]
    cows.sort()

    for permutation in permutations(cows):
        cow_positions = dict()
        for idx, cow in enumerate(permutation):
            cow_positions[cow] = idx

        meet_all_constraints = True
        for cow1, cow2 in constraints:
            if abs(cow_positions[cow1] - cow_positions[cow2]) != 1:
                meet_all_constraints = False
                break
        if meet_all_constraints:
            return permutation


def main():
    with open("lineup.in", "r") as fin:
        N = int(fin.readline().strip())
        constraints = []
        for _ in range(N):
            constraint = fin.readline().strip().split()
            constraints.append((constraint[0], constraint[-1]))

    cows = solve(constraints)
    with open("lineup.out", "w") as fout:
        for cow in cows:
            fout.write(f"{cow}\n")


def test():
    for i in range(1, 10):
        with open(f"cow_lineup_test_data/{i}.in", "r") as fin:
            N = int(fin.readline().strip())
            constraints = []
            for _ in range(N):
                constraint = fin.readline().strip().split()
                constraints.append((constraint[0], constraint[-1]))

        cows = solve(constraints)
        with open(f"test_outs/{i}.out", "w") as fout:
            for cow in cows:
                fout.write(f"{cow}\n")


if __name__ == "__main__":
    test()
