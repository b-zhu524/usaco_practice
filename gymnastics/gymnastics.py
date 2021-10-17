from itertools import combinations


class Cow:
    rankings = None
    K = None
    N = None

    def __init__(self, position):
        self.pos = position

    def is_better(self, other, round_num):
        self_pos = 0
        other_pos = 0
        for i in range(Cow.N):
            if Cow.rankings[round_num][i] == self.pos:
                self_pos = i
            elif Cow.rankings[round_num][i] == other.pos:
                other_pos = i
        return self_pos < other_pos

    def is_consistent(self, other):
        lt_count = 0
        for round_num in range(Cow.K):
            if self.is_better(other, round_num):
                lt_count += 1
        if lt_count == 0 or lt_count == Cow.K:
            return True
        return False


def solve(K, N, rankings):
    Cow.rankings = rankings
    Cow.K = K
    Cow.N = N

    consistent_count = 0
    cows = rankings[0]
    for c1, c2 in combinations(cows, 2):
        cow1, cow2 = Cow(c1), Cow(c2)
        if cow1.is_consistent(cow2):
            consistent_count += 1
    return consistent_count


def main():
    with open("gymnastics.in", "r") as fin:
        K, N = map(int, fin.readline().strip().split())
        rankings = []
        for i in range(K):
            current_scores = [int(score) for score in fin.readline().strip().split()]
            rankings.append(current_scores)
    with open("gymnastics.out", "w") as fout:
        fout.write(f"{solve(K, N, rankings)}\n")


def test():
    for j in range(1, 11):
        with open(f"gymnastics_test_data/{j}.in", "r") as fin:
            K, N = map(int, fin.readline().strip().split())
            rankings = []
            for i in range(K):
                current_scores = [int(score) for score in fin.readline().strip().split()]
                rankings.append(current_scores)
        with open(f"test_outs/{j}.out", "w") as fout:
            fout.write(f"{solve(K, N, rankings)}\n")


if __name__ == "__main__":
    test()
