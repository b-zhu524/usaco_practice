# def procedure(swaps, shells):
#     score = 0
#     for swap in swaps:
#         a, b, g = swap
#         shells[a], shells[b] = shells[b], shells[a]
#         if shells[g] == 1:
#             score += 1
#     return score
#
#
# def solve(swaps):
#     # pebble under 0
#     shells = [-1, 1, 0, 0]
#     score = procedure(swaps, shells)
#
#     # pebble under 1
#     shells = [-1, 0, 1, 0]
#     score = max(score, procedure(swaps, shells))
#
#     # pebble under 2
#     shells = [-1, 0, 0, 1]
#     score = max(score, procedure(swaps, shells))
#
#     return score


def procedure(swaps, pebble_idx):
    score = 0
    for a, b, g in swaps:
        if a == pebble_idx:
            pebble_idx = b
        elif b == pebble_idx:
            pebble_idx = a
        if g == pebble_idx:
            score += 1
    return score


def solve(swaps):
    # pebble under 1
    pebble_idx = 1
    score = procedure(swaps, pebble_idx)

    # pebble under 2
    pebble_idx = 2
    score = max(score, procedure(swaps, pebble_idx))

    # pebble under 3
    pebble_idx = 3
    score = max(score, procedure(swaps, pebble_idx))

    return score


def main():
    with open("shell.in", "r") as fin:
        N = int(fin.readline().strip())
        swap_guesses = []
        for _ in range(N):
            a, b, g = [int(x) for x in (fin.readline().strip().split())]
            swap_guesses.append((a, b, g))

    with open("shell.out", "w") as fout:
        fout.write(str(solve(swap_guesses)))


def test():
    for i in range(1, 11):
        with open(f"shell_game_test_data/{i}.in", "r") as fin:
            N = int(fin.readline().strip())
            swap_guesses = []
            for _ in range(N):
                temp_swap_guess = list(map(int, (fin.readline().strip().split())))
                swap_guesses.append(temp_swap_guess)

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{(solve(swap_guesses))}\n")


if __name__ == "__main__":
    main()
