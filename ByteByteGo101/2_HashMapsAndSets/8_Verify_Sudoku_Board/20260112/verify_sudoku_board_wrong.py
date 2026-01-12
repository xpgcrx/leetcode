from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:
    # この記述方法だと、全要素同じset()の参照になってしまうので、
    # ロジックは正しいがWrong Answerになる
    row = [set()] * 9
    col = [set()] * 9
    subgrid = [[set()] * 3] * 3
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

    
