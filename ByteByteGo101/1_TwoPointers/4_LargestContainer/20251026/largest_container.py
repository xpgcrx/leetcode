from typing import List

def largest_container(heights: List[int]) -> int:
    left = 0
    right = len(heights) - 1
    largest = 0
    while left < right:
        x = right - left
        y = min(heights[left], heights[right])
        water = x * y
        largest = max(largest, water)
        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left +=1
            right -= 1
    return largest
