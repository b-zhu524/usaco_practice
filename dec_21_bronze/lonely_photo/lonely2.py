def lonely_cow_subsets(idx, start_lonely, end_lonely):
    left = idx - start_lonely - 1
    right = end_lonely - idx - 1
    return left * right + max(left-1, 0) + max(right-1, 0)


def solve(n, cows, left, right):
    res = 0
    for i in range(n):
        l = i - 1
        if l >= 0 and cows[l] != cows[i]:
            l = left[l]
        r = i + 1
        if r < n and cows[r] != cows[i]:
            r = right[r]
        num_subsets = lonely_cow_subsets(i, l, r)
        res += num_subsets
    return res


def main():
    with open("lonely.in", "r") as fin:
        n = int(fin.readline().strip())
        cows = fin.readline().strip()
        stack = [0]
        right = [n for _ in range(n)]
        for i in range(n):
            if cows[i] != cows[stack[-1]]:
                while stack:
                    j = stack.pop()
                    right[j] = i
            stack.append(i)

        stack = [n - 1]
        left = [-1 for _ in range(n)]
        for i in range(n - 2, -1, -1):
            if cows[i] != cows[stack[-1]]:
                while stack:
                    j = stack.pop()
                    left[j] = i
            stack.append(i)
        print(left, right)

    with open("lonely.out", "w") as fout:
        fout.write(f"{solve(n, cows, left, right)}\n")


def test():
    for k in range(1, 12):
        with open(f"lonely_photo_test_data/{k}.in", "r") as fin:
            n = int(fin.readline().strip())
            cows = fin.readline().strip()
            stack = [0]
            right = [n for _ in range(n)]
            for i in range(n):
                if cows[i] != cows[stack[-1]]:
                    while stack:
                        j = stack.pop()
                        right[j] = i
                stack.append(i)

            stack = [n - 1]
            left = [-1 for _ in range(n)]
            for i in range(n - 2, -1, -1):
                if cows[i] != cows[stack[-1]]:
                    while stack:
                        j = stack.pop()
                        left[j] = i
                stack.append(i)

        with open(f"test_outs/{k}.out", "w") as fout:
            fout.write(f"{solve(n, cows, left, right)}\n")


if __name__ == '__main__':
    test()
