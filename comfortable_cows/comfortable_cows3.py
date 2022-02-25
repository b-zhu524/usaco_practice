def find_neighbor(pasture, x, y):
    num_neighbors = 0
    if x > 1000 or x < 0 or y > 1000 or y < 0:
        return -1
    if not pasture[x][y]:
        return -1

    # top
    if y < 1000 and pasture[x][y+1] == 1:
        num_neighbors += 1
    # left
    if x > 0 and pasture[x-1][y] == 1:
        num_neighbors += 1

    # right
    if x < 1000 and pasture[x+1][y] == 1:
        num_neighbors += 1

    # bottom
    if y > 0 and pasture[x][y-1] == 1:
        num_neighbors += 1

    return num_neighbors


def solve(n, coords):
    pasture = [[0 for _ in range(1001)] for _ in range(1001)]
    comfortable_list = []
    comfortable_cnt = 0
    for x, y in coords:
        pasture[x][y] = 1

        num_neighbors = find_neighbor(pasture, x, y)
        if num_neighbors == 3:
            comfortable_cnt += 1
        if num_neighbors == 4:
            comfortable_cnt -= 1

        num_neighbors = find_neighbor(pasture, x+1, y)
        if num_neighbors == 3:
            comfortable_cnt += 1
        elif num_neighbors == 4:
            comfortable_cnt -= 1

        num_neighbors = find_neighbor(pasture, x-1, y)
        if num_neighbors == 3:
            comfortable_cnt += 1
        elif num_neighbors == 4:
            comfortable_cnt -= 1

        num_neighbors = find_neighbor(pasture, x, y+1)
        if num_neighbors == 3:
            comfortable_cnt += 1
        elif num_neighbors == 4:
            comfortable_cnt -= 1

        num_neighbors = find_neighbor(pasture, x, y-1)
        if num_neighbors == 3:
            comfortable_cnt += 1
        elif num_neighbors == 4:
            comfortable_cnt -= 1
        comfortable_list.append(comfortable_cnt)
    return comfortable_list


def main():
    with open(f"comfortable.in", "r") as fin:
        n = int(fin.readline().strip())
        coords = []
        for _ in range(n):
            coord = fin.readline().strip().split()
            coords.append((int(coord[0]), int(coord[1])))

    res = solve(n, coords)
    with open(f"comfortable.out", "w") as fout:
        for cc in res:
            fout.write(f"{cc}\n")


def test():
    for i in range(1, 13):
        with open(f"comfortable_cows_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            coords = []
            for _ in range(n):
                coord = fin.readline().strip().split()
                coords.append((int(coord[0]), int(coord[1])))

        res = solve(n, coords)
        with open(f"test_outs/{i}.out", "w") as fout:
            for cc in res:
                fout.write(f"{cc}\n")


if __name__ == '__main__':
    test()
