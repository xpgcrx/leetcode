from typing import List


# Time: O(n)
# Space: O(1)
def shift_zeros_to_the_end(nums: List[int]) -> None:
    zero_counter = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_counter += 1
        else:
            nums[i - zero_counter] = nums[i]

    for i in range(len(nums) - zero_counter, len(nums)):
        nums[i] = 0
