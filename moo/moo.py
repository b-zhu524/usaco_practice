def get_k_from_n(n):
    k = 0
    sl = 3
    while sl < n:
        sl = sl * 2 + (k+3)
        k += 1
    return k


def str_len(k, cache):
    if k == -1:
        return 0
    if k in cache:
        return cache[k]
    length = str_len(k-1, cache) * 2 + (k+3)
    cache[k] = length
    return length


def what_letter(n, k, cache):
    left_str_len = str_len(k-1, cache)
    mid_str_len = k + 3

    if left_str_len < n <= (left_str_len + mid_str_len):
        if n == left_str_len + 1:
            return "m"
        return "o"

    if n > (left_str_len + mid_str_len):
        return what_letter(n - (left_str_len + mid_str_len), k-1, cache)

    if n < (left_str_len + mid_str_len):
        return what_letter(n, k-1, cache)


def solve(N):
    cache = dict()
    k = get_k_from_n(N)
    res = what_letter(N, k, cache)
    return res


def main():
    with open("moo.in", "r") as fin:
        N = int(fin.readline().strip())
    with open("moo.out", "w") as fout:
        fout.write(f"{solve(N)}\n")


def test():
    for i in range(1, 11):
        with open(f"moo_test_data/{i}.in", "r") as fin:
            N = int(fin.readline().strip())
        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(N)}\n")


if __name__ == '__main__':
    test()
