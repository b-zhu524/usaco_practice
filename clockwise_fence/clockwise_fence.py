def solve(fence):
    deg_cnt = 0
    fence.append(fence[0])
    for i in range(len(fence)-1):
        # positive 90
        if (fence[i], fence[i+1]) == ("N", "E") or (fence[i], fence[i+1]) == ("E", "S") or (fence[i], fence[i+1]) == \
                ("S", "W") or (fence[i], fence[i+1]) == ("W", "N"):
            deg_cnt += 90

        # negative 90
        if (fence[i], fence[i+1]) == ("E", "N") or (fence[i], fence[i+1]) == ("S", "E") or (fence[i], fence[i+1]) == \
                ("W", "S") or (fence[i], fence[i+1]) == ("N", "W"):
            deg_cnt -= 90
    if deg_cnt < 0:
        return "CCW"
    return "CW"


def main():
    with open(f"clockwise_fence.in", "r") as fin:
        n = int(fin.readline().strip())
        fences = []
        for _ in range(n):
            temp = fin.readline().strip()
            new_fence = [x for x in temp]
            fences.append(new_fence)
    with open(f"clockwise_fence.out", "w") as fout:
        for i in range(n):
            fout.write(f"{solve(fences[i])}\n")


def test():
    for j in range(1, 11):
        with open(f"clockwise_fence_test_data/{j}.in", "r") as fin:
            n = int(fin.readline().strip())
            fences = []
            for _ in range(n):
                temp = fin.readline().strip()
                new_fence = [x for x in temp]
                fences.append(new_fence)
        with open(f"test_outs/{j}.out", "w") as fout:
            for i in range(n):
                fout.write(f"{solve(fences[i])}\n")


if __name__ == '__main__':
    test()
