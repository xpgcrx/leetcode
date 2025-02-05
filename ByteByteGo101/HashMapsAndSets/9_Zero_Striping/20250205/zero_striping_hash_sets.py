from typing import List


def zero_striping(matrix: List[List[int]]) -> None:
    if not matrix:
        return
    row_zeros = set()
    column_zeros = set()
    m = len(matrix)
    n = len(matrix[0])
    for r in range(m):
        for c in range(n):
            num = matrix[r][c]
            if num == 0:
                row_zeros.add(r)
                column_zeros.add(c)

    # row_zeros = {1,4}
    # column_zeros = {1,4}
    for r in range(m):
        for c in range(n):
            if r in row_zeros or c in column_zeros:
                matrix[r][c] = 0
