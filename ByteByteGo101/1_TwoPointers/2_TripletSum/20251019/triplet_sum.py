from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    snums = sorted(nums)
    triplet = set()
    for i in range(len(snums)):
        target = -snums[i]
        left = i + 1 
        right = len(snums) - 1
        while left < right:
            s = snums[left] + snums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                triplet.add((snums[i], snums[left], snums[right]))
                left += 1
    return [list(t) for t in triplet]

