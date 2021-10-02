def number_neighbors(x, y, pasture):
    num_neighbor = 0
    if x > 1000 or x < 0 or y > 1000 or y < 0:
        return -1

    if not pasture[x][y]:
        return -1

    if x+1 <= 1000 and pasture[x+1][y]:
        num_neighbor += 1
    if x-1 >= 0 and pasture[x-1][y]:
        num_neighbor += 1
    if y+1 <= 1000 and pasture[x][y+1]:
        num_neighbor += 1
    if y-1 >= 0 and pasture[x][y-1]:
        num_neighbor += 1
    return num_neighbor


def solve(cows):
    pasture = [[0 for _ in range(1001)] for _ in range(1001)]
    comfortable_count = 0
    all_iters_result = []

    for x, y in cows:
        pasture[x][y] = 1

        num_neighbors = number_neighbors(x, y, pasture)
        if num_neighbors == 3:
            comfortable_count += 1
        elif num_neighbors == 4:
            comfortable_count -= 1

        num_neighbors = number_neighbors(x+1, y, pasture)
        if num_neighbors == 3:
            comfortable_count += 1
        elif num_neighbors == 4:
            comfortable_count -= 1

        num_neighbors = number_neighbors(x-1, y, pasture)
        if num_neighbors == 3:
            comfortable_count += 1
        elif num_neighbors == 4:
            comfortable_count -= 1

        num_neighbors = number_neighbors(x, y+1, pasture)
        if num_neighbors == 3:
            comfortable_count += 1
        elif num_neighbors == 4:
            comfortable_count -= 1

        num_neighbors = number_neighbors(x, y-1, pasture)
        if num_neighbors == 3:
            comfortable_count += 1
        elif num_neighbors == 4:
            comfortable_count -= 1
        all_iters_result.append(comfortable_count)
    return all_iters_result


def main():
    N = int(input())
    cows = []
    for i in range(N):
        x, y = input().strip().split()
        cows.append((int(x), int(y)))

    for result in solve(cows):
        print(f"{result}")


def test():
    for j in range(1, 13):
        with open(f"comfortable_cows_test_data/{j}.in", "r") as fin:
            N = int(fin.readline().strip())
            cows = []
            for i in range(N):
                x, y = fin.readline().strip().split()
                cows.append((int(x), int(y)))
        with open(f"test_outs/{j}.out", "w") as fout:
            result = solve(cows)
            for count in result:
                fout.write(f"{count}\n")


if __name__ == "__main__":
    test()
