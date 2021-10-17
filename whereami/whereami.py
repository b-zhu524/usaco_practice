def solve(N, farms):
    for size in range(1, N+1):
        substrings = set()
        unique = True
        for start in range(N-size+1):
            end = start + size
            substring = farms[start:end]
            if substring in substrings:
                unique = False
                break
            else:
                substrings.add(substring)

        if unique:
            return size


def main():
    with open("whereami.in", "r") as fin:
        N = int(fin.readline().strip())
        farms = fin.readline().strip()
    with open("whereami.out", "w") as fout:
        fout.write(f"{solve(N, farms)}\n")


def test():
    for i in range(1, 11):
        with open(f"whereami_test_data/{i}.in", "r") as fin:
            N = int(fin.readline().strip())
            farms = fin.readline().strip()
        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(N, farms)}\n")


if __name__ == '__main__':
    test()
