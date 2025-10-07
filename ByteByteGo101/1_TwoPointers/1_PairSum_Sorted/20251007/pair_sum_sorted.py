from typing import List

# Time: O(n)
# Space: O(1)
def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1
    while left < right:
        cal = nums[left] + nums[right]
        if cal < target:
            left += 1
        elif cal > target:
            right -= 1
        else:
            return [left, right]
    return []
