from itertools import combinations


def x_parallel(c1, c2):
    if c1[1] == c2[1]:
        return True
    return False


def y_parallel(c1, c2):
    if c1[0] == c2[0]:
        return True
    return False


def area(c1, c2, c3):
    l1 = abs(c2[0] - c1[0])
    l2 = abs(c3[1] - c2[1])
    return l2*l1


def solve(coords):
    max_area = 0
    for c1, c2, c3 in combinations(coords, 3):
        if x_parallel(c1, c2):
            if y_parallel(c2, c3):
                curr_area = area(c1, c2, c3)
            elif y_parallel(c1, c3):
                curr_area = area(c2, c1, c3)
            else:
                continue

        elif x_parallel(c2, c3):
            if y_parallel(c1, c2):
                curr_area = area(c3, c2, c1)
            elif y_parallel(c1, c3):
                curr_area = area(c2, c3, c1)
            else:
                continue

        elif x_parallel(c1, c3):
            if y_parallel(c1, c2):
                curr_area = area(c3, c1, c2)
            elif y_parallel(c2, c3):
                curr_area = area(c1, c3, c2)
            else:
                continue

        else:
            continue

        if curr_area > max_area:
            max_area = curr_area

    return max_area


def main():
    with open("triangles.in", "r") as fin:
        n = int(fin.readline().strip())
        coords = []
        for _ in range(n):
            x, y = fin.readline().strip().split()
            coords.append((int(x), int(y)))

    res = solve(coords)
    with open("triangles.out", "w") as fout:
        fout.write(f"{res}\n")


def test():
    for i in range(1, 11):
        with open(f"triangles_bronze_feb20/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            coords = []
            for _ in range(n):
                x, y = fin.readline().strip().split()
                coords.append((int(x), int(y)))

        res = solve(coords)
        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{res}\n")


if __name__ == '__main__':
    test()
