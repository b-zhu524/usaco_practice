def is_used(seed, neighbors, pasture_seeds):
    for neighbor in neighbors:
        if neighbor in pasture_seeds and pasture_seeds[neighbor] == seed:
            return True
    return False


def solve(N, graph):
    pasture_seeds = dict()

    for p in range(1, N + 1):
        if p not in graph:  # p has no neighbor
            pasture_seeds[p] = 1
            continue

        neighbors = graph[p]
        for seed in (1, 2, 3, 4):
            if not is_used(seed, neighbors, pasture_seeds):
                pasture_seeds[p] = seed
                break
    return pasture_seeds


def main():
    with open("revegetate.in", "r") as fin:
        graph = dict()
        N, M = [int(item) for item in fin.readline().strip().split()]

        for _ in range(M):
            past1, past2 = [int(item) for item in fin.readline().strip().split()]
            if past1 not in graph:
                graph[past1] = [past2]
            else:
                graph[past1].append(past2)

            if past2 not in graph:
                graph[past2] = [past1]
            else:
                graph[past2].append(past1)

    res = solve(N, graph)
    with open("revegetate.out", "w") as fout:
        for p in range(1, N+1):
            fout.write(f"{res[p]}")
        fout.write("\n")


def test():
    for i in range(1, 11):
        with open(f"revegetate_test_data/{i}.in", "r") as fin:
            graph = dict()
            N, M = [int(item) for item in fin.readline().strip().split()]

            for _ in range(M):
                past1, past2 = [int(item) for item in fin.readline().strip().split()]
                if past1 not in graph:
                    graph[past1] = [past2]
                else:
                    graph[past1].append(past2)

                if past2 not in graph:
                    graph[past2] = [past1]
                else:
                    graph[past2].append(past1)

        res = solve(N, graph)
        with open(f"test_outs/{i}.out", "w") as fout:
            for p in range(1, N+1):
                fout.write(f"{res[p]}")
            fout.write("\n")


if __name__ == "__main__":
    test()
