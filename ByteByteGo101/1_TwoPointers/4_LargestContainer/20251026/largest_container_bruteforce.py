from typing import List

def largest_container(heights: List[int]) -> int:
    largest = 0
    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            x = j - i
            y = min(heights[i], heights[j])
            water = x * y
            largest = max(water, largest)
    return largest
