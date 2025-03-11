from typing import List


# Time: O(n)
# Space: O(1)
def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return []
