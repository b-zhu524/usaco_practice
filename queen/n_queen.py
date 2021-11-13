def under_attack(board, new_x, new_y):
    # horizontal
    n = len(board)
    for square in board[new_x]:
        if square != 0:
            return True

    # diagonal left

    x, y = new_x, new_y
    while 0 <= x < n and 0 <= y < n:
        if board[x][y] != 0:
            return True
        x -= 1
        y -= 1

    x, y = new_x, new_y
    while 0 <= x < n and 0 <= y < n:
        if board[x][y] != 0:
            return True
        x -= 1
        y += 1

    return False


# new

def under_attack_new(n, row_status, diagonal_right_status, diagonal_left_status, new_x, new_y):
    new_row_idx = new_x
    new_diag_right_idx = new_x + new_y
    new_diag_left_idx = (n - 1 - new_x) + new_y

    if row_status[new_row_idx]:
        return True
    if diagonal_right_status[new_diag_right_idx]:
        return True
    if diagonal_left_status[new_diag_left_idx]:
        return True

    return False


def print_board(board):
    for row in board:
        print(row)


def nq(board, row_status, diagonal_right_status, diagonal_left_status, col):
    n = len(board)

    # base
    if col >= n:
        print_board(board)
        print()
        return

    # update
    for row in range(n):
        if under_attack_new(n, row_status, diagonal_right_status, diagonal_left_status, row, col):
            continue

        board[row][col] = 1
        row_status[row] = True
        diagonal_right_status[row+col] = True
        diagonal_left_status[(n-1-row)+col] = True

        # recursion
        nq(board, row_status, diagonal_right_status, diagonal_left_status, col+1)

        # undo
        diagonal_left_status[(n-1-row)+col] = False
        diagonal_right_status[row+col] = False
        row_status[row] = False
        board[row][col] = 0


def main():
    n = 5
    board = [[0 for _ in range(n)] for _ in range(n)]
    row_status = [False for _ in range(n)]
    diagonal_right_status = [False for _ in range(n*2-1)]
    diagonal_left_status = [False for _ in range(n*2-1)]
    nq(board, row_status, diagonal_right_status, diagonal_left_status, col=0)


if __name__ == "__main__":
    main()
