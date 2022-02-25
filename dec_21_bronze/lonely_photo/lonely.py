def lonely_cow_subsets(idx, start_lonely, end_lonely):
    left = idx - start_lonely
    right = end_lonely - start_lonely - left
    return left * right + max(left-1, 0) + max(right-1, 0)


def solve(n, cows):
    res = 0
    for i in range(n):
        start_lonely = i
        end_lonely = i

        while start_lonely > 0 and cows[start_lonely-1] != cows[i]:
            start_lonely -= 1

        while end_lonely < n-1 and cows[end_lonely+1] != cows[i]:
            end_lonely += 1

        curr_res = lonely_cow_subsets(i, start_lonely, end_lonely)
        res += curr_res
    return res


def main():
    with open("lonely.in", "r") as fin:
        n = int(fin.readline().strip())
        cows = fin.readline().strip()

    with open("lonely.out", "w") as fout:
        fout.write(f"{solve(n, cows)}\n")


def test():
    for i in range(1, 12):
        with open(f"lonely_photo_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            cows = fin.readline().strip()

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, cows)}\n")


if __name__ == '__main__':
    test()
