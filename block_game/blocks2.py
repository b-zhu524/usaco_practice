def count_letters(word):
    alpha_counter = [0] * 26
    for letter in word:
        letter_idx = ord(letter) - ord("a")
        alpha_counter[letter_idx] += 1
    return alpha_counter


def solve(n, boards):
    final_alpha_counter = [0] * 26
    for word1, word2 in boards:
        w1_counter = count_letters(word1)
        w2_counter = count_letters(word2)

        for i in range(26):
            final_alpha_counter[i] += max(w1_counter[i], w2_counter[i])
    return final_alpha_counter


def main():
    with open("blocks.in", "r") as fin:
        n = int(fin.readline().strip())
        boards = []
        for _ in range(n):
            w1, w2 = fin.readline().strip().split()
            boards.append((w1, w2))

    res = solve(n, boards)
    with open("blocks.out", "w") as fout:
        for letter in res:
            fout.write(f"{letter}\n")


def test():
    for i in range(1, 11):
        with open(f"block_game_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            boards = []
            for _ in range(n):
                w1, w2 = fin.readline().strip().split()
                boards.append((w1, w2))

        res = solve(n, boards)
        with open(f"test_outs/{i}.out", "w") as fout:
            for letter in res:
                fout.write(f"{letter}\n")


if __name__ == "__main__":
    test()
