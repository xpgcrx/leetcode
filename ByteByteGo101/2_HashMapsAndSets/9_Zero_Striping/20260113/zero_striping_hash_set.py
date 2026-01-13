from typing import List

def zero_striping(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return
    m = len(matrix)
    n = len(matrix[0])
    row_sets = set()
    col_sets = set()
    for i in range(m):
        for j in range(n):
            num = matrix[i][j]
            if num == 0:
                row_sets.add(i)
                col_sets.add(j)
    for i in range(m):
        for j in range(n):
            num = matrix[i][j]
            if i in row_sets or j in col_sets:
                matrix[i][j] = 0


