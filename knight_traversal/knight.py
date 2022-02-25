def is_valid(board, row, col):
    n = len(board)
    if n > row >= 0 and n > col >= 0 and board[row][col] == -1:
        return True
    return False


def kt(board, row, col, moves, step):
    n = len(board)
    if step == n * n:
        print(board)
        print()
        return True

    found_solution = False
    for move_row, move_col in moves:
        # update
        if not is_valid(board, row + move_row, col + move_col):
            continue
        row += move_row
        col += move_col
        board[row][col] = step

        # recursion
        if kt(board, row, col, moves, step + 1):
            found_solution = True
            return board

        # undo
        board[row][col] = -1
        col -= move_col
        row -= move_row
    return found_solution


def main():
    N = 5
    board = [[-1 for _ in range(N)] for _ in range(N)]
    board[0][0] = 0
    moves = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, -2), (1, 2), (-1, -2), (-1, 2))
    res = kt(board, 0, 0, moves, 1)
    print(res)


if __name__ == "__main__":
    main()
