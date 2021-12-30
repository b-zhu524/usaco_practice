from collections import deque


def bfs(pathways, node):
    visited = set()
    visited_list = [node]
    q = deque()

    visited.add(node)
    q.append(node)

    while q:
        v = q.popleft()
        for u in pathways[v]:
            if u not in visited:
                visited.add(u)
                visited_list.append(u)
                q.append(u)

    return visited_list


def check_neighbors(colors, pathways, curr_field):
    neighbors = pathways[curr_field]

    min_color = -1
    curr_colors = set()
    for n in neighbors:
        curr_colors.add(colors[n])

    while min_color in curr_colors:
        min_color += 1

    return min_color


def check_neighbor_neighbors(colors, pathways, curr_field):
    neighbors = pathways[curr_field]
    min_color = -1

    neighbor_neighbors = []
    nn_colors = set()

    for n in neighbors:
        nns = pathways[n]
        for nn in nns:
            if nn == curr_field:
                continue
            neighbor_neighbors.append(nn)
            nn_colors.add(colors[nn])

    while min_color in nn_colors:
        min_color += 1

    return min_color


def solve(n, pathways):
    fields = bfs(pathways, 1)
    colors = dict()
    all_colors = set()
    num_colors = 0

    for i in range(1, n+1):
        colors[i] = -1

    for field in fields:
        n_min_color = check_neighbors(colors, pathways, field)
        nn_min_color = check_neighbor_neighbors(colors, pathways, field)

        c = max(n_min_color, nn_min_color)
        if c not in all_colors:
            num_colors += 1
        colors[field] = c
        all_colors.add(c)

    return num_colors


def main():
    with open("planting.in", "r") as fin:
        n = int(fin.readline().strip())
        pathways = dict()
        for _ in range(n-1):
            p1, p2 = fin.readline().strip().split()
            p1, p2 = int(p1), int(p2)

            if p1 not in pathways:
                pathways[p1] = [p2]
            else:
                pathways[p1].append(p2)

            if p2 not in pathways:
                pathways[p2] = [p1]
            else:
                pathways[p2].append(p1)

    with open("planting.out", "w") as fout:
        fout.write(f"{solve(n, pathways)}\n")


def test():
    for i in range(1, 11):
        with open(f"grass_planting_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            pathways = dict()
            for _ in range(n - 1):
                p1, p2 = fin.readline().strip().split()
                p1, p2 = int(p1), int(p2)

                if p1 not in pathways:
                    pathways[p1] = [p2]
                else:
                    pathways[p1].append(p2)

                if p2 not in pathways:
                    pathways[p2] = [p1]
                else:
                    pathways[p2].append(p1)

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, pathways)}\n")


if __name__ == '__main__':
    test()
