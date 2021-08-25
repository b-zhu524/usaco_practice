def solve(a, heard):
    heard_idx = 0
    alphabet_idx = 0
    num_iters = 0
    heard_len = len(heard)
    alphabet_len = len(a)

    while heard_idx < heard_len:
        if alphabet_idx == alphabet_len:
            alphabet_idx = 0

        if alphabet_idx == 0:
            num_iters += 1

        if a[alphabet_idx] == heard[heard_idx]:
            heard_idx += 1
            alphabet_idx += 1
        else:
            alphabet_idx += 1

    return num_iters


if __name__ == "__main__":
    alpha = input()
    heard = input()
    counter = solve(alpha, heard)
    print(counter)
