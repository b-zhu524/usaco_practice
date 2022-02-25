from itertools import combinations


def find_individual_win(rows):
    wins = 0
    # row
    for row in rows:
        if row[0] == row[1] == row[2]:
            wins += 1

    # column
    for i in range(3):
        if rows[i][0] == rows[i][1] == rows[i][2]:
            wins += 1

    # diagonals
    if rows[0][0] == rows[1][1] == rows[2][2]:
        wins += 1
    if rows[0][2] == rows[1][1] == rows[2][0]:
        wins += 1

    return wins


def find_team_wins(rows, member1, member2):
    wins = 0

    # rows
    for row in rows:
        if (row[0] == member1 or row[0] == member2) and \
                (row[1] == member1 or row[1] == member2) and \
                (row[1] == member1 or row[1] == member2):
            wins += 1

    # column
    for i in range(3):
        if (rows[i][0] == member1 or rows[i][0] == member2) and \
                (rows[i][1] == member1 or rows[i][1] == member2) and \
                (rows[i][2] == member1 or rows[i][2] == member2):
            wins += 1

    # diagonals
    if (rows[0][0] == member1 or rows[0][0] == member2) and \
            (rows[1][1] == member1 or rows[1][1] == member2) and\
            (rows[2][2] == member1 or rows[2][2] == member2):
        wins += 1
    if (rows[0][2] == member1 or rows[0][2] == member2) and \
            (rows[1][1] == member1 or rows[1][1] == member2) and \
            (rows[2][0] == member1 or rows[2][0] == member2):
        wins += 1

    return wins


def solve(cows, rows):
    individual_wins = find_individual_win(rows)
    team_wins = 0

    for c1, c2 in combinations(cows, 2):
        team_wins += find_team_wins(rows, c1, c2)

    return individual_wins, team_wins


def main():
    with open("tttt.in", "r") as fin:
        rows = []
        cows = ""
        for _ in range(3):
            row = fin.readline().strip()
            rows.append(row)
            cows += row

    individual_wins, team_wins = solve(cows, rows)
    with open("tttt.out", "w") as fout:
        fout.write(f"{individual_wins}\n")
        fout.write(f"{team_wins}\n")


if __name__ == '__main__':
    main()
