def build_dict(coordinate_list):
    x_dict = dict()
    y_count = dict()

    for x, y in coordinate_list:
        if x not in x_dict:
            x_dict[x] = set()
        x_dict[x].add((x, y))

        if y not in y_count:
            y_count[y] = 1
        else:
            y_count[y] += 1

    return x_dict, y_count


def remove_one_col(x, x_dict, y_count):
    y_count_copy = y_count.copy()
    for _, y in x_dict[x]:
        y_count_copy[y] -= 1
        if y_count_copy[y] == 0:
            del y_count_copy[y]
    return y_count_copy


def check(coordinate_list):
    x_dict, y_count = build_dict(coordinate_list)

    # all cows <= 3 rows
    if len(y_count) <= 3:
        return 1

    # 1 col + 2 row
    for x in x_dict:
        y_count_after_remove_one_col = remove_one_col(x, x_dict, y_count)
        if len(y_count_after_remove_one_col) <= 2:
            return 1
    return 0


def solve(coordinate_list):
    # check row first
    if check(coordinate_list):
        return 1

    # check col
    for cow in coordinate_list:
        cow[0], cow[1] = cow[1], cow[0]
    return check(coordinate_list)


def main():
    with open("3lines.in", "r") as fin:
        N = int(fin.readline().strip())
        coordinate_list = []
        for _ in range(N):
            x, y = fin.readline().strip().split()
            x, y = int(x), int(y)
            coordinate_list.append([x, y])

    res = solve(coordinate_list)
    with open("3lines.out", "w") as fout:
        fout.write(f"{res}\n")


def test():
    for i in range(1, 21):
        with open(f"3_lines_test_data/{i}.in", "r") as fin:
            N = int(fin.readline().strip())
            coordinate_list = []
            for _ in range(N):
                x, y = fin.readline().strip().split()
                x, y = int(x), int(y)
                coordinate_list.append([x, y])

        res = solve(coordinate_list)
        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{res}\n")


if __name__ == '__main__':
    test()
