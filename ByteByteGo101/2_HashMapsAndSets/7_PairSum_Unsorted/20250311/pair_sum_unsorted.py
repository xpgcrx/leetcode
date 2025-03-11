from typing import List


# Time: O(n)
# Space: O(n)
def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    d = {}
    for i, n in enumerate(nums):
        sub = target - n
        if n in d:
            return [d[n], i]
        d[sub] = i
    return []
