from collections import defaultdict
from typing import List


def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    left_map = defaultdict(int)
    right_map = defaultdict(int)
    count = 0

    for x in nums:
        right_map[x] += 1

    for x in nums:
        right_map[x] -= 1
        if x % r == 0:
            count += left_map[x // r] * right_map[x * r]
        left_map[x] += 1
    return count
