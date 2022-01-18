from itertools import combinations


def x_parallel(p1, p2):
    return p1[1] == p2[1]


def y_parallel(p1, p2):
    return p1[0] == p2[0]


def solve(n, points):
    largest_area = 0
    for p1, p2, p3 in combinations(points, 3):
        if x_parallel(p1, p2):
            x_len = abs(p1[0]-p2[0])
            if y_parallel(p1, p3):
                y_len = abs(p1[1]-p3[1])
                largest_area = max(largest_area, x_len*y_len)
            if y_parallel(p2, p3):
                y_len = abs(p2[1]-p3[1])
                largest_area = max(largest_area, x_len * y_len)

        if x_parallel(p1, p3):
            x_len = abs(p1[0]-p3[0])
            if y_parallel(p1, p2):
                y_len = abs(p1[1]-p2[1])
                largest_area = max(largest_area, x_len * y_len)

            if y_parallel(p2, p3):
                y_len = abs(p2[1]-p3[1])
                largest_area = max(largest_area, x_len * y_len)

        if x_parallel(p2, p3):
            x_len = abs(p2[0]-p3[0])
            if y_parallel(p1, p2):
                y_len = abs(p1[1]-p2[1])
                largest_area = max(largest_area, x_len * y_len)

            if y_parallel(p1, p3):
                y_len = abs(p1[1]-p3[1])
                largest_area = max(largest_area, x_len * y_len)

    return largest_area


def main():
    with open(f"triangles.in", "r") as fin:
        n = int(fin.readline().strip())
        points = []
        for _ in range(n):
            p1, p2 = fin.readline().strip().split()
            points.append([int(p1), int(p2)])

    with open(f"triangles.out", "w") as fout:
        fout.write(f"{solve(n, points)}\n")


def test():
    for i in range(1, 10):
        with open(f"triangles_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            points = []
            for _ in range(n):
                p1, p2 = fin.readline().strip().split()
                points.append([int(p1), int(p2)])

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, points)}\n")


if __name__ == '__main__':
    test()
