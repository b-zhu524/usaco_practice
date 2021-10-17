def is_consistent(cow1, cow2, rankings, K):
    counter = 0
    for ranking in rankings:
        idx1 = ranking[cow1]
        idx2 = ranking[cow2]
        if idx1 < idx2:
            counter += 1
    if counter == 0 or counter == K:
        return True
    return False


def solve(K, N, rankings):
    consistent_count = 0
    for cow1 in range(1, N):
        for cow2 in range(cow1+1, N+1):
            if is_consistent(cow1, cow2, rankings, K):
                consistent_count += 1
    return consistent_count


def main():
    with open("gymnastics.in", "r") as fin:
        K, N = map(int, fin.readline().strip().split())
        rankings = []
        for i in range(K):
            current_scores = [int(score) for score in fin.readline().strip().split()]
            ranking = dict()
            for idx, cow_id in enumerate(current_scores):
                ranking[cow_id] = idx
            rankings.append(ranking)
    with open("gymnastics.out", "w") as fout:
        fout.write(f"{solve(K, N, rankings)}\n")


def test():
    for j in range(1, 11):
        with open(f"gymnastics_test_data/{j}.in", "r") as fin:
            K, N = map(int, fin.readline().strip().split())
            rankings = []
            for i in range(K):
                current_scores = [int(score) for score in fin.readline().strip().split()]
                ranking = dict()
                for idx, cow_id in enumerate(current_scores):
                    ranking[cow_id] = idx
                rankings.append(ranking)
        with open(f"test_outs/{j}.out", "w") as fout:
            fout.write(f"{solve(K, N, rankings)}\n")


if __name__ == "__main__":
    test()
