from typing import List


def largest_container(heights: List[int]) -> int:
    water_max = 0
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            water = (j - i) * min(heights[i], heights[j])
            water_max = max(water, water_max)
    return water_max
