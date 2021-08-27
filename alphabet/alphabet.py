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


def faster_solve(a, heard):
    heard_len = len(heard)
    a_dict = {}

    for idx, letter in enumerate(a):
        a_dict[letter] = idx

    num_iters = 0
    for i in range(1, heard_len):
        if a_dict[heard[i]] <= a_dict[heard[i-1]]:
            num_iters += 1

    num_iters += 1
    return num_iters


def main():
    alpha = input()
    heard = input()
    counter = faster_solve(alpha, heard)
    print(counter)


if __name__ == '__main__':
    main()
