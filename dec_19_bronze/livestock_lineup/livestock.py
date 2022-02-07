from itertools import permutations


def solve(n, neighbors):
    print(neighbors)
    cows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
    cows.sort()
    for p in permutations(cows):
        cow_position = dict()
        for idx, cow in enumerate(p):
            cow_position[cow] = idx
        flag = False
        for c in neighbors:
            ns = neighbors[c]
            for neigh in ns:
                if abs(cow_position[neigh] - cow_position[c]):
                    flag = True
                    break
            if flag:
                break
        if not flag:
            return p


def main():
    with open(f"livestock.in", "r") as fin:
        n = int(fin.readline().strip())
        neighbors = dict()

        for _ in range(n):
            sequence = fin.readline().strip().split()
            c1, c2 = sequence[0], sequence[-1]
            if c1 in neighbors:
                neighbors[c1].append(c2)
            else:
                neighbors[c1] = [c2]

            if c2 in neighbors:
                neighbors[c2].append(c1)
            else:
                neighbors[c2] = [c1]

    with open(f"livestock.out", "w") as fout:
        fout.write(f"{solve(n, neighbors)}\n")


if __name__ == '__main__':
    main()
