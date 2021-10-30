def is_used(seed, neighbors, past_seeds):
    for neighbor in neighbors:
        if neighbor == seed and past_seeds[neighbor] == seed:
            return True
    return False


def solve(N, M, graph):
    past_seeds = dict()

    for past in range(1, M+1):
        if past not in graph:
            past_seeds[past] = 1
            continue

        neighbors = graph[past]
        for seed in (1, 2, 3, 4):
            if not is_used(seed, neighbors, past_seeds):
                past_seeds[past] = seed
                break
    return past_seeds


def main():
    with open("revegetate.in", "r") as fin:
        graph = dict()
        N, M = [int(item) for item in fin.readline().strip().split()]

        for i in range(M):
            past1, past2 = [item for item in fin.readline().strip().split()]
            if past1 not in graph:
                graph[past1] = [past2]
            else:
                graph[past1].append(past2)

            if past2 not in graph:
                graph[past2] = [past2]
            else:
                graph[past2].append(past1)


if __name__ == "__main__":
    main()
