from typing import List


# Time: O(n^2)
# Space: O(n^2)
def verify_sudoku_board(board: List[List[int]]) -> bool:
    row_sets = [set() for _ in range(9)]
    column_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]
    for i in range(9):
        for j in range(9):
            n = board[i][j]

            if n == 0:
                continue

            if n in row_sets[i]:
                return False
            if n in column_sets[j]:
                return False
            if n in subgrid_sets[i // 3][j // 3]:
                return False

            row_sets[i].add(n)
            column_sets[j].add(n)
            subgrid_sets[i // 3][j // 3].add(n)
    return True
