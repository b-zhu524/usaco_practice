def solve(N, cow_ids):
    unique_ids = tuple(set(cow_ids))
    best_in_row = 0
    for i in range(len(unique_ids)):
        current_cow_ids = []
        for j in range(N):
            if cow_ids[j] != unique_ids[i]:
                current_cow_ids.append(cow_ids[j])
        all_in_row = [1]
        for k in range(len(current_cow_ids)):
            if k != 0 and current_cow_ids[k] == current_cow_ids[k-1]:
                all_in_row[-1] += 1
            else:
                all_in_row.append(1)
        max_in_row = max(all_in_row)
        if max_in_row > best_in_row:
            best_in_row = max_in_row
    return best_in_row


def solve2(N, cow_ids):
    unique_ids = set(cow_ids)
    if len(unique_ids) == 1:
        return N

    best_in_row = 0

    for to_be_removed in unique_ids:
        current_cow_ids = []
        # build new list with 1 id removed
        for cow_id in cow_ids:
            if cow_id != to_be_removed:
                current_cow_ids.append(cow_id)
        # count maximum consecutive ids
        count = 0
        best_count = 0
        prev_cow = None
        for curr_cow in current_cow_ids:
            if curr_cow != prev_cow:
                best_count = max(best_count, count)
                count = 1
            else:
                count += 1
            prev_cow = curr_cow
        # in case last count is best
        best_count = max(best_count, count)

        best_in_row = max(best_in_row, best_count)
    return best_in_row


def main():
    with open("cowrow.in", "r") as fin:
        N = int(fin.readline().strip())
        cow_ids = []
        for i in range(N):
            cow = int(fin.readline().strip())
            cow_ids.append(cow)

    with open("cowrow.out", "w") as fout:
        fout.write(f"{solve(N, cow_ids)}\n")


def test():
    for j in range(1, 23):
        with open(f"cowrow_test_data/{j}.in", "r") as fin:
            N = int(fin.readline().strip())
            cow_ids = []
            for i in range(N):
                cow = int(fin.readline().strip())
                cow_ids.append(cow)

        with open(f"test_outs/{j}.out", "w") as fout:
            fout.write(f"{solve2(N, cow_ids)}\n")


if __name__ == "__main__":
    test()
