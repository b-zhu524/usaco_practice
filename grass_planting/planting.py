from collections import deque


def bfs(pathways):
    pass


def solve():
    pass


def main():
    with open("planting.in", "r") as fin:
        n = int(fin.readline().strip())
        pathways = dict()
        for i in range(1, n+1):
            p1, p2 = fin.readline().strip().split()

            if p1 not in pathways:
                pathways[p1] = [p2]
            else:
                pathways[p1].append(p2)

            if p2 not in pathways:
                pathways[p2] = p1
            else:
                pathways[p2].append(p1)

    with open("planting.out", "w") as fout:
        pass


if __name__ == '__main__':
    main()
