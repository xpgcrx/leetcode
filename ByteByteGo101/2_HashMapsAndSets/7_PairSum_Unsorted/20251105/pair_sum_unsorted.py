from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    m = {}
    for i, n in enumerate(nums):
        if n in m:
            return [m[n], i]
        c = target - n
        m[c] = i
    return []
