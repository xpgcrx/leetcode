from typing import List


# Time: O(n)
# Space: O(1)
def largest_container(heights: List[int]) -> int:
    left = 0
    right = len(heights) - 1
    max_water = 0
    while left < right:
        w = right - left
        h = min(heights[left], heights[right])
        max_water = max(max_water, w * h)
        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return max_water
