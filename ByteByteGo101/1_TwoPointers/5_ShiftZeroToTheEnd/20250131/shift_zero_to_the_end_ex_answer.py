from typing import List


def shift_zeros_to_the_end(nums: List[int]) -> None:
    # the 'left' pointer is used to position non-zero elements.
    left = 0
    # Iterate throught the array using a 'right' pointer to locate non-zero elements.
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            # Increment 'left' since it now points to a position already occupied
            # by a non-zero elements.
            left += 1
