def solve(n, ids):
    ps = [ids[0]]
    for i in range(1, n):
        ps.append(ps[-1] + ids[i])

    max_size = 0
    for i in range(n-1, -1, -1):
        for j in range(i-1):
            if ps[i] % 7 == 0:
                if i+1 > max_size:
                    max_size = i+1
                break

            if ps[i] % 7 == ps[j] % 7:
                if i - j + 1 > max_size:
                    max_size = i-j
                break
    return max_size


def main():
    with open(f"div7.in", "r") as fin:
        n = int(fin.readline().strip())
        ids = []
        for _ in range(n):
            ids.append(int(fin.readline().strip()))

    with open(f"div7.out", "r") as fout:
        print(solve(n, ids))


def test():
    for i in range(1, 11):
        with open(f"summing_to_sevens_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            ids = []
            for _ in range(n):
                ids.append(int(fin.readline().strip()))

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, ids)}\n")


if __name__ == '__main__':
    test()
