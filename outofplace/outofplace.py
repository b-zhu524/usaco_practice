# does not work

def outofplace(n, cows, remove_i):
    if remove_i != 0:
        prev_cow = cows[0]
    else:
        prev_cow = cows[1]
    for i in range(1, n):
        if i == remove_i:
            continue
        if cows[i] < prev_cow:
            return True
        prev_cow = cows[i]
    return False


def solve(n, cows):
    # find out of place
    for i in range(n):
        if not outofplace(n, cows, i):
            bessie = i
    new_cows = sorted(list(set(cows)))
    for i in range(len(new_cows)):
        if new_cows[i] == cows[bessie]:
            sorted_bessie_idx = i
            break
    return abs(bessie - sorted_bessie_idx - 1)


def main():
    with open("outofplace.in", "r") as fin:
        n = int(fin.readline().strip())
        cows = []
        for _ in range(n):
            cows.append(int(fin.readline().strip()))
    with open("outofplace.out", "w") as fout:
        fout.write(f"{solve(n, cows)}\n")


def test():
    for i in range(1, 11):
        with open(f"outofplace_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            cows = []
            for _ in range(n):
                cows.append(int(fin.readline().strip()))
        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, cows)}\n")


if __name__ == '__main__':
    test()
