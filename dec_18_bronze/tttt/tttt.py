from itertools import combinations


def diagonal_vict(c, board):
    if board[0][0] == c and board[1][1] == c and board[2][2] == c:
        return True
    if board[0][2] == c and board[1][1] == c and board[2][0] == c:
        return True
    return False


def row_vict(c, board):
    for row in board:
        if row[0] == c and row[1] == c and row[2] == c:
            return True
    return False


def col_vict(c, board):
    for i in range(3):
        if board[0][i] == c and board[1][i] == c and board[2][i] == c:
            return True
    return False


def diagonal_vict_2(c1, c2, board):
    c1_cnt = 0
    c2_cnt = 0
    if board[0][0] == c1 or board[0][0] == c2:
        if board[0][0] == c1:
            c1_cnt += 1
        else:
            c2_cnt += 1
        if board[1][1] == c1 or board[1][1] == c2:
            if board[1][1] == c1:
                c1_cnt += 1
            else:
                c2_cnt += 1
            if board[2][2] == c1 or board[2][2] == c2:
                if board[2][2] == c1:
                    c1_cnt += 1
                else:
                    c2_cnt += 1
                if c1_cnt and c2_cnt:
                    return True

    c1_cnt = 0
    c2_cnt = 0
    if board[2][0] == c1 or board[2][0] == c2:
        if board[2][0] == c1:
            c1_cnt += 1
        else:
            c2_cnt += 1
        if board[1][1] == c1 or board[1][1] == c2:
            if board[1][1] == c1:
                c1_cnt += 1
            else:
                c2_cnt += 1
            if board[0][2] == c1 or board[0][2] == c2:
                if board[0][2] == c1:
                    c1_cnt += 1
                else:
                    c2_cnt += 1

                if c1_cnt and c2_cnt:
                    return True
    return False


def row_vict_2(c1, c2, board):
    for row in board:
        c1_cnt = 0
        c2_cnt = 0
        if row[0] == c1 or row[0] == c2:
            if row[0] == c1:
                c1_cnt += 1
            else:
                c2_cnt += 1
            if row[1] == c1 or row[1] == c2:
                if row[1] == c1:
                    c1_cnt += 1
                else:
                    c2_cnt += 1
                if row[2] == c1 or row[2] == c2:
                    if row[2] == c1:
                        c1_cnt += 1
                    else:
                        c2_cnt += 1
                    if c1_cnt and c2_cnt:
                        return True
    return False


def col_vict_2(c1, c2, board):
    for i in range(3):
        c1_cnt = 0
        c2_cnt = 0
        if board[0][i] == c1 or board[0][i] == c2:
            if board[0][i] == c1:
                c1_cnt += 1
            else:
                c2_cnt += 1
            if board[1][i] == c1 or board[1][i] == c2:
                if board[1][i] == c1:
                    c1_cnt += 1
                else:
                    c2_cnt += 1
                if board[2][i] == c1 or board[2][i] == c2:
                    if board[2][i] == c1:
                        c1_cnt += 1
                    else:
                        c2_cnt += 1
                    if c1_cnt and c2_cnt:
                        return True
    return False


def solve(board, cows):
    # individual victories
    individual_cnt = 0
    for c in cows:
        if row_vict(c, board) or diagonal_vict(c, board) or col_vict(c, board):
            individual_cnt += 1

    # team victories
    team_cnt = 0
    for c1, c2 in combinations(cows, 2):
        if row_vict_2(c1, c2, board) or col_vict_2(c1, c2, board) or diagonal_vict_2(c1, c2, board):
            team_cnt += 1

    return individual_cnt, team_cnt


def main():
    with open("tttt.in", "r") as fin:
        board = []
        cows = set()
        for _ in range(3):
            r = fin.readline().strip()
            board.append(r)
            for c in r:
                cows.add(c)

    i, t = solve(board, cows)
    with open("tttt.out", "w") as fout:
        fout.write(f"{i}\n")
        fout.write(f"{t}\n")
#
#
# def test():
#     for j in range(1, 11):
#         with open(f"tttt_test_data/{j}.in", "r") as fin:
#             board = []
#             cows = set()
#             for _ in range(3):
#                 r = fin.readline().strip()
#                 board.append(r)
#                 for c in r:
#                     cows.add(c)
#
#         i, t = solve(board, cows)
#         with open(f"test_outs/{j}.out", "w") as fout:
#             fout.write(f"{i}\n")
#             fout.write(f"{t}\n")


if __name__ == '__main__':
    main()
