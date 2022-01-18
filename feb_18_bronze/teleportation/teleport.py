def solve(a, b, x, y):
    min_dist = 1001

    # a -> b
    d = abs(a-b)
    min_dist = min(d, min_dist)

    # a -> y -> x -> b
    d = abs(a-y) + abs(x-b)
    min_dist = min(d, min_dist)

    # a -> x -> y -> b
    d = abs(a-x) + abs(b-y)
    min_dist = min(d, min_dist)

    return min_dist


def main():
    with open("teleport.in", "r") as fin:
        a, b, x, y = fin.readline().strip().split()

    with open("teleport.out", "w") as fout:
        fout.write(f"{solve(a, b, x, y)}\n")


def test():
    for i in range(1, 11):
        with open(f"teleportation_test_data/{i}.in", "r") as fin:
            a, b, x, y = fin.readline().strip().split()
            a, b, x, y = int(a), int(b), int(x), int(y)

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(a, b, x, y)}\n")


if __name__ == '__main__':
    test()
