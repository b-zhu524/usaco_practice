def solve(n, mailboxes):
    for size in range(1, n+1):
        substrings = set()
        flag = False
        for start in range(n-size+1):
            new_substring = mailboxes[start:start+size]
            if new_substring in substrings:
                flag = True
                break
            substrings.add(new_substring)
        if not flag:
            return size


def main():
    with open(f"whereami.in", "r") as fin:
        n = int(fin.readline().strip())
        mailboxes = fin.readline().strip()

    with open(f"whereami.out", "w") as fout:
        fout.write(f"{solve(n, mailboxes)}\n")


def test():
    for i in range(1, 11):
        with open(f"whereami_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            mailboxes = fin.readline().strip()

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, mailboxes)}\n")


if __name__ == '__main__':
    test()
