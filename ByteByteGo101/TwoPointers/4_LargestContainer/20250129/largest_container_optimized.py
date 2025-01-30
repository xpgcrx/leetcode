from typing import List


# Time: O(n)
# Space: O(1)
def largest_container(heights: List[int]) -> int:
    water_max = 0
    # start from max width
    left, right = 0, len(heights) - 1
    while left < right:
        water = (right - left) * min(heights[left], heights[right])
        water_max = max(water, water_max)
        if heights[left] < heights[right]:
            left += 1
        elif heights[right] < heights[left]:
            right -= 1
        else:
            left += 1
            right -= 1
    return water_max
