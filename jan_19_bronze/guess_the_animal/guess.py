from itertools import combinations


def in_common_cnt(animals, a1, a2):
    cnt = 0
    for char in animals[a1]:
        if char in animals[a2]:
            cnt += 1
    return cnt


def solve(n, animals):
    max_common_cnt = -1
    for a1, a2 in combinations(animals, 2):
        in_common = in_common_cnt(animals, a1, a2)
        if in_common > max_common_cnt:
            max_common_cnt = in_common
    return max_common_cnt + 1


def main():
    with open(f"guess.in", "r") as fin:
        n = int(fin.readline().strip())
        animals = dict()
        for _ in range(n):
            a, _, *adjs = fin.readline().strip().split()
            animals[a] = set()
            for adj in adjs:
                animals[a].add(adj)

    res = solve(n, animals)
    with open(f"guess.out", "w") as fout:
        fout.write(f"{res}\n")


def test():
    for i in range(1, 11):
        with open(f"guess_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            animals = dict()
            for _ in range(n):
                a, _, *adjs = fin.readline().strip().split()
                animals[a] = set()
                for adj in adjs:
                    animals[a].add(adj)

        res = solve(n, animals)
        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{res}\n")


if __name__ == '__main__':
    test()
