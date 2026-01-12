from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    subgrid =[[set() for _ in range(3)] for _ in range(3)]
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == 0:
                continue
            if num in row[i]:
                return False
            if num in col[j]:
                return False
            if num in subgrid[i//3][j//3]:
                return False
            row[i].add(num)
            col[j].add(num)
            subgrid[i//3][j//3].add(num)
    return True

    
