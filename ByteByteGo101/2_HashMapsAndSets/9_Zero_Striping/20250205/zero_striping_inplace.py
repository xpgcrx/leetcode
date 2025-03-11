from typing import List

# https://bytebytego.com/exercises/coding-patterns/hash-maps-and-sets/zero-striping


# Time: O(m) + O(n) + O(mn) = O(mn)
# Space: O(1)
def zero_striping(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    m = len(matrix)
    n = len(matrix[0])

    # Check if the first row initially contains a zero.
    first_row_contains_zeros = False
    for c in range(n):
        if matrix[0][c] == 0:
            first_row_contains_zeros = True

    # Check if the first column initially contains a zero.
    first_column_contains_zeros = False
    for r in range(m):
        if matrix[r][0] == 0:
            first_column_contains_zeros = True

    # Use the first row and column as markers.
    # If an element in the submatrix is zero,
    # mark its corresponding row and column
    # in the first row and column as 0.
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    # Update the submatrix using the markers
    # in the first row and column.
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    # If the first row had a zero initially,
    # set all elements in the first row to zero.
    for c in range(n):
        if first_row_contains_zeros:
            matrix[0][c] = 0

    # If the first column had a zero initially,
    # set all elements in the first column to zero.
    for r in range(m):
        if first_column_contains_zeros:
            matrix[r][0] = 0
