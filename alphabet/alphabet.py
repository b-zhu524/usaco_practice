
def solve(a, heard):
    heard_idx = 0
    alphabet_idx = 0
    num_iters = 0
    heard_len = len(heard)
    alphabet_len = len(a)
    match = False
    while heard_idx < heard_len:
        if a[alphabet_idx] == heard[heard_idx]:
            heard_idx += 1
            match = True
        alphabet_idx += 1
        if alphabet_idx == alphabet_len:
            num_iters += 1
            alphabet_idx = 0
            match = False
    if match:
        num_iters += 1

    # print(alphabet_idx, heard_idx)
    # if alphabet_idx == alphabet_len:
    #     alphabet_idx = 0
    # if a[alphabet_idx] == heard[heard_idx]:
    #     heard_idx += 1
    # if a[alphabet_idx] == a[0]:
    #     num_iters += 1
    #     print(num_iters, a[alphabet_idx], heard_idx)
    # alphabet_idx += 1

    return num_iters


if __name__ == "__main__":
    alpha = input()
    heard = input()
    print(solve(alpha, heard))
