def is_used(seed, graph, past_seeds):
    pass


def solve(N, M, pastures):
    pass


def main():
    with open("revegetate.in", "r") as fin:
        N, M = [item for item in fin.readline().strip().split()]
        graph = [[0 for _ in range(N)] for _ in range(N)]

        for past1, past2 in fin.readline().strip().split():
            past1, past2 = int(past1), int(past2)
            graph[past1-1][past2-1] = 1
            graph[past2-1][past1-1] = 1

    with open("revegetate.out", "w") as fout:
        pass


if __name__ == "__main__":
    main()
