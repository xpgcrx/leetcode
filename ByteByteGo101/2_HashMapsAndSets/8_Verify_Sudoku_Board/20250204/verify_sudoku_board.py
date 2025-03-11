from typing import List


def verify_sudoku_board(board: List[List[int]]) -> bool:
    row_sets = [set() for _ in range(9)]
    column_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == 0:
                continue
            if num in row_sets[i]:
                return False
            if num in column_sets[j]:
                return False
            if num in subgrid_sets[i // 3][j // 3]:
                return False

            row_sets[i].add(num)
            column_sets[j].add(num)
            subgrid_sets[i // 3][j // 3].add(num)
    return True
