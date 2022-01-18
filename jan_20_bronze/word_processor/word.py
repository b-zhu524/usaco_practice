def solve(n, k, words, word_len):
    i = 0
    format_words = []
    while True:
        curr_words = []
        curr_sum = 0
        while i < n and curr_sum <= k:
            if curr_sum + word_len[i] > k:
                break
            curr_sum += word_len[i]
            curr_words.append(words[i])
            i += 1
        format_words.append(curr_words)
        if i >= n:
            break
    return format_words


def main():
    with open(f"word.in", "r") as fin:
        n, k = fin.readline().strip().split()
        n, k = int(n), int(k)
        words = fin.readline().strip().split()
        word_len = []
        for word in words:
            word_len.append(len(word))

    res = solve(n, k, words, word_len)
    with open(f"word.out", "w") as fout:
        for line in res:
            for i in range(len(line)):
                fout.write(f"{line[i]}")
                if i != len(line)-1:
                    fout.write(" ")
            fout.write("\n")


def test():
    for j in range(1, 11):
        with open(f"word_processor_test_data/{j}.in", "r") as fin:
            n, k = fin.readline().strip().split()
            n, k = int(n), int(k)
            words = fin.readline().strip().split()
            word_len = []
            for word in words:
                word_len.append(len(word))

        res = solve(n, k, words, word_len)
        with open(f"test_outs/{j}.out", "w") as fout:
            for line in res:
                for i in range(len(line)):
                    fout.write(f"{line[i]}")
                    if i != len(line) - 1:
                        fout.write(" ")
                fout.write("\n")


if __name__ == '__main__':
    test()
