from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1
    while left < right:
        sum_value = nums[left] + nums[right]
        if sum_value < target:
            left += 1
        elif target < sum_value:
            right -= 1
        else:
            return [left, right]
    return []
