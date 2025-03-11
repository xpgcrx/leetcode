from typing import List


# Time: O(m * n)
# Space: O(1)
def zero_striping(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    m = len(matrix)
    n = len(matrix[0])

    first_row_contains_zero = False
    for c in range(n):
        if matrix[0][c] == 0:
            first_row_contains_zero = True

    first_column_contains_zero = False
    for r in range(m):
        if matrix[r][0] == 0:
            first_column_contains_zero = True

    for r in range(1, m):
        for c in range(1, n):
            x = matrix[r][c]
            if x == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    for r in range(1, m):
        for c in range(1, n):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if first_row_contains_zero:
        for c in range(n):
            matrix[0][c] = 0

    if first_column_contains_zero:
        for r in range(m):
            matrix[r][0] = 0
