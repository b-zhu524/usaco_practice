def next_cow_by_constraints(line, neighbors):
    if len(line) == 0:
        return None
    curr_cow = line[-1]
    if curr_cow not in neighbors:
        return None
    cow_neighbors = neighbors[curr_cow]
    if len(cow_neighbors) == 1:
        if len(line) >= 2 and line[-2] == cow_neighbors[0]:
            return None
        else:
            return cow_neighbors[0]
    else:
        prev_cow = line[-2]
        for neighbor in cow_neighbors:
            if neighbor != prev_cow:
                return neighbor


def solve(neighbors):
    cows = ["Bessie", "Buttercup", "Belinda", "Beatrice",
            "Bella", "Blue", "Betsy", "Sue"]
    cows.sort()

    line = []
    cows_in_line = set()

    for cow in cows:
        # cow is already in line
        if cow in cows_in_line:
            continue
        # cow does not have any neighbor constraint
        if cow not in neighbors:
            line.append(cow)
            cows_in_line.add(cow)
            continue

        # cow has neighbor constraint
        cow_neighbors = neighbors[cow]
        if len(cow_neighbors) == 1 or (len(line) > 0 and line[-1] in cow_neighbors):
            line.append(cow)
            cows_in_line.add(cow)

            next_neighbor = next_cow_by_constraints(line, neighbors)
            while next_neighbor is not None:
                line.append(next_neighbor)
                cows_in_line.add(next_neighbor)
                next_neighbor = next_cow_by_constraints(line, neighbors)
    return line


def main():
    with open("lineup.in", "r") as fin:
        N = int(fin.readline().strip())
        neighbors = dict()
        for _ in range(N):
            constraint = fin.readline().strip().split()
            cow1 = constraint[0]
            cow2 = constraint[-1]
            if cow1 in neighbors:
                neighbors[cow1].append(cow2)
            else:
                neighbors[cow1] = [cow2]

            if cow2 in neighbors:
                neighbors[cow2].append(cow1)
            else:
                neighbors[cow2] = [cow1]

    cows = solve(neighbors)
    with open("lineup.out", "w") as fout:
        for cow in cows:
            fout.write(f"{cow}\n")


def test():
    for i in range(1, 11):
        with open(f"cow_lineup_test_data/{i}.in", "r") as fin:
            N = int(fin.readline().strip())
            neighbors = dict()
            for _ in range(N):
                constraint = fin.readline().strip().split()
                cow1 = constraint[0]
                cow2 = constraint[-1]
                if cow1 in neighbors:
                    neighbors[cow1].append(cow2)
                else:
                    neighbors[cow1] = [cow2]

                if cow2 in neighbors:
                    neighbors[cow2].append(cow1)
                else:
                    neighbors[cow2] = [cow1]

        cows = solve(neighbors)
        with open(f"test_outs/{i}.out", "w") as fout:
            for cow in cows:
                fout.write(f"{cow}\n")


if __name__ == "__main__":
    main()
    test()
