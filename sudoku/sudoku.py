def print_board(board):
    for row in board:
        print(row)


def is_valid(board, curr_row_status, curr_col_status, curr_box_status, new_num):
    if new_num in curr_row_status or new_num in curr_col_status or new_num in curr_box_status:
        return False
    return True


def sudoku(board, row_status, col_status, box_status, step):
    n = len(board)
    if step == n*n:
        print_board(board)
        print()
        return

    row_idx = step // 9
    col_idx = step % 9
    box_idx = row_idx // 3 * 3 + col_idx // 3

    if board[row_idx][col_idx] != 0:
        sudoku(board, row_status, col_status, box_status, step+1)
    else:
        numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        # update
        for num in numbers:
            if not is_valid(board, row_status[row_idx], col_status[col_idx], box_status[box_idx], num):
                continue
            board[row_idx][col_idx] = num
            row_status[row_idx].add(num)
            col_status[col_idx].add(num)
            box_status[box_idx].add(num)

            sudoku(board, row_status, col_status, box_status, step+1)

            box_status[box_idx].remove(num)
            col_status[col_idx].remove(num)
            row_status[row_idx].remove(num)
            board[row_idx][col_idx] = 0


def main():
    n = 9
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    row_status = [set() for _ in range(n)]
    col_status = [set() for _ in range(n)]
    box_status = [set() for _ in range(n)]

    for row in range(n):
        for col in range(n):
            num = board[row][col]
            if num:
                row_status[row].add(num)
                col_status[col].add(num)
                box_status[row // 3 * 3 + col // 3].add(num)

    sudoku(board, row_status, col_status, box_status, step=0)


if __name__ == '__main__':
    main()
