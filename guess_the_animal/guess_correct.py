from itertools import combinations


def in_common_count(animals, animal1, animal2):
    in_common = 0
    for description in animals[animal1]:
        if description in animals[animal2]:
            in_common += 1
    return in_common


def solve(animals):
    max_in_common = 0
    for a1, a2 in combinations(animals, 2):
        in_common = in_common_count(animals, a1, a2)
        if in_common > max_in_common:
            max_in_common = in_common
    return max_in_common + 1


def main():
    with open("guess.in", "r") as fin:
        n = int(fin.readline().strip())
        animals = dict()
        for _ in range(n):
            animal, count, *descriptions = fin.readline().strip().split()
            animals[animal] = descriptions

    res = solve(animals)
    with open("guess.out", "w") as fout:
        fout.write(f"{res}\n")


def test():
    for i in range(1, 11):
        with open(f"guess_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            animals = dict()
            for _ in range(n):
                animal, count, *descriptions = fin.readline().strip().split()
                animals[animal] = set()
                for description in descriptions:
                    animals[animal].add(description)

        res = solve(animals)
        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{res}\n")


if __name__ == '__main__':
    test()
