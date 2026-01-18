from typing import List
from collections import defaultdict

def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    count = 0

    left = defaultdict(int)
    right = defaultdict(int)

    for n in nums:
        right[n] += 1

    for n in nums:
        if right[n] > 0: # この分岐は不要（nはrightに必ず有るので）
            right[n] -= 1

        if n % r == 0:
            count += left[n//r] * right[n*r]

        left[n] += 1
    return count

        

