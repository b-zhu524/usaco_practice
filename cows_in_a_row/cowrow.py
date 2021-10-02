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
            fout.write(f"{solve(N, cow_ids)}\n")


if __name__ == "__main__":
    test()
