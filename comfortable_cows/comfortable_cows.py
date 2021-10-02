def count_neighbor(pasture, x, y):
    neighbor_count = 0
    if x < 0 or x > 1000 or y < 0 or y > 1000:
        return -1

    if pasture[x][y] == 0:
        return -1

    if x+1 <= 1000 and pasture[x+1][y]:
        neighbor_count += 1
    if y+1 <= 1000 and pasture[x][y+1]:
        neighbor_count += 1
    if x-1 >= 0 and pasture[x-1][y]:
        neighbor_count += 1
    if y-1 >= 0 and pasture[x][y-1]:
        neighbor_count += 1
    return neighbor_count


def solve(cows):
    pasture = [[0 for _ in range(1001)] for _ in range(1001)]
    comfortable_counter = 0
    result = []
    for x, y in cows:
        pasture[x][y] = 1

        if count_neighbor(pasture, x, y) == 3:
            comfortable_counter += 1

        neighbor_count = count_neighbor(pasture, x+1, y)
        if neighbor_count == 3:
            comfortable_counter += 1
        elif neighbor_count == 4:
            comfortable_counter -= 1

        neighbor_count = count_neighbor(pasture, x, y+1)
        if neighbor_count == 3:
            comfortable_counter += 1
        elif neighbor_count == 4:
            comfortable_counter -= 1

        neighbor_count = count_neighbor(pasture, x-1, y)
        if neighbor_count == 3:
            comfortable_counter += 1
        elif neighbor_count == 4:
            comfortable_counter -= 1

        neighbor_count = count_neighbor(pasture, x, y-1)
        if neighbor_count == 3:
            comfortable_counter += 1
        elif neighbor_count == 4:
            comfortable_counter -= 1
        result.append(comfortable_counter)
    return result


def main():
    N = int(input())
    cows = []
    for i in range(N):
        x, y = input().strip().split()
        cows.append((int(x), int(y)))
    result = solve(cows)
    for count in result:
        print(count)


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
