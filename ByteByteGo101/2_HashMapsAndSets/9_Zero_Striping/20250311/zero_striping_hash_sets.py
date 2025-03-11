from typing import List


# Time: O(m * n)
# Space: O(m + n)
def zero_striping(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    m = len(matrix)
    n = len(matrix[0])
    row_sets = [set() for _ in range(m)]
    column_sets = [set() for _ in range(n)]

    for i in range(m):
        for j in range(n):
            x = matrix[i][j]
            row_sets[i].add(x)
            column_sets[j].add(x)

    for i in range(m):
        for j in range(n):
            if 0 in row_sets[i] or 0 in column_sets[j]:
                matrix[i][j] = 0
