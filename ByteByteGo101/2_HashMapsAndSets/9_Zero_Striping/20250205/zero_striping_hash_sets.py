from typing import List


# Time: O(mn)
# Space: O(m + n)
def zero_striping(matrix: List[List[int]]) -> None:
    if not matrix:
        return
    row_zeros = set()
    column_zeros = set()
    m = len(matrix)
    n = len(matrix[0])

    # Pass 1: Traverse through the matrix to identify the rows and
    # columns containing zeros and store their indexes in the
    # appropriate hash sets.
    for r in range(m):
        for c in range(n):
            num = matrix[r][c]
            if num == 0:
                row_zeros.add(r)
                column_zeros.add(c)

    # Pass 2: Set any cell in the matrix to zero if its row index is
    # in 'row_zeros' or its column index is in 'column_zeros'.
    for r in range(m):
        for c in range(n):
            if r in row_zeros or c in column_zeros:
                matrix[r][c] = 0
