from typing import List

# Time: O(n^3)
# Space: O(n^2)
def triplet_sum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums) # avoid duplicates
    triplet = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet.add((nums[i], nums[j], nums[k]))
    return [list(t) for t in triplet]
