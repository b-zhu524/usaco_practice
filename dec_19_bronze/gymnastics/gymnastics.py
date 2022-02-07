from itertools import combinations


def consistent(n, k, c1, c2, lineup):
    status = None
    for line in lineup:
        if line[c1] > line[c2]:
            new_status = 1
        else:
            new_status = 0
        if status is None or new_status == status:
            status = new_status
            continue
        return False
    return True


def solve(n, k, lineup, cow_list):
    consistent_cnt = 0
    for c1, c2 in combinations(cow_list, 2):
        if consistent(n, k, c1, c2, lineup):
            consistent_cnt += 1
    return consistent_cnt


def main():
    with open("gymnastics.in", "r") as fin:
        n, k = fin.readline().strip().split()
        n, k = int(n), int(k)
        lineup = []
        for _ in range(n):
            temp = fin.readline().strip().split()
            temp = [int(x) for x in temp]
            cows = dict()
            for i in range(k):
                cows[temp[i]] = i
            lineup.append(cows)

    with open("gymnastics.out", "w") as fout:
        fout.write(f"{solve(n, k, lineup, temp)}\n")


def test():
    for j in range(1, 11):
        with open(f"gymnastics_test_data/{j}.in", "r") as fin:
            n, k = fin.readline().strip().split()
            n, k = int(n), int(k)
            lineup = []
            for _ in range(n):
                temp = fin.readline().strip().split()
                temp = [int(x) for x in temp]
                cows = dict()
                for i in range(k):
                    cows[temp[i]] = i
                lineup.append(cows)

        with open(f"test_outs/{j}.out", "w") as fout:
            fout.write(f"{solve(n, k, lineup, temp)}\n")


if __name__ == '__main__':
    test()
