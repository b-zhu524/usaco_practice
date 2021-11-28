def is_valid(pasture, next_x, next_y):
    if 0 > next_x or 4 < next_x or 0 > next_y or 4 < next_y:
        return False
    elif pasture[next_x][next_y] != 1:
        return False
    return True


def solve(K, pasture, curr_x, curr_y, num_solutions, step):
    if curr_x == 4 and curr_y == 4 and step < 25 - K - 1:
        return

    if step == 25 - K - 1:
        if curr_x == 4 and curr_y == 4:
            num_solutions[0] += 1
        return

    moves = [(curr_x+1, curr_y), (curr_x-1, curr_y), (curr_x, curr_y+1), (curr_x, curr_y-1)]
    for next_x, next_y in moves:
        if not is_valid(pasture, next_x, next_y):
            continue

        pasture[next_x][next_y] = 0

        solve(K, pasture, next_x, next_y, num_solutions, step+1)

        pasture[next_x][next_y] = 1


def main():
    pasture = [[1 for _ in range(5)] for _ in range(5)]
    pasture[0][0] = 0

    with open("grazing.in", "r") as fin:
        K = int(fin.readline().strip())
        for _ in range(K):
            empt_x, empt_y = fin.readline().strip().split()
            empt_x, empt_y = int(empt_x), int(empt_y)
            empt_x -= 1
            empt_y -= 1
            pasture[empt_x][empt_y] = 0

    res = [0]
    solve(K, pasture, 0, 0, res, step=0)

    with open("grazing.out", "w") as fout:
        fout.write(f"{res[0]}\n")


def test():
    for i in range(1, 11):
        pasture = [[1 for _ in range(5)] for _ in range(5)]
        pasture[0][0] = 0

        with open(f"grazing_test_data/{i}.in", "r") as fin:
            K = int(fin.readline().strip())
            for _ in range(K):
                empt_x, empt_y = fin.readline().strip().split()
                empt_x, empt_y = int(empt_x), int(empt_y)
                empt_x -= 1
                empt_y -= 1
                pasture[empt_x][empt_y] = 0

        res = [0]
        solve(K, pasture, 0, 0, res, step=0)

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{res[0]}\n")


if __name__ == "__main__":
    test()
