def find_h_idx(citations):
    citations.sort(reverse=True)
    cnt = 0
    h = (0, 0)
    for c in citations:
        cnt += 1
        if c < cnt:
            break
        h = (cnt, min(c, cnt))
    return h


def solve(L, citations):
    curr_idx, curr_h = find_h_idx(citations)

    if L == 0 or curr_idx >= len(citations):
        return curr_h

    citations[curr_idx] += 1
    L -= 1

    idx = curr_idx - 1
    while idx >= 0 and citations[idx] == curr_h and L > 0:
        citations[idx] += 1
        idx -= 1
        L -= 1

    _, new_h = find_h_idx(citations)
    return new_h


def main():
    N, L = [int(item) for item in input().split()]
    citations = [int(citation) for citation in input().split()]
    print(f"{solve(L, citations)}\n")


def test():
    for i in range(1, 18):
        with open(f"acowdemia1_test_data/{i}.in", "r") as fin:
            N, L = [int(item) for item in fin.readline().strip().split()]
            citations = [int(citation) for citation in fin.readline().strip().split()]

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(L, citations)}\n")


if __name__ == "__main__":
    test()
