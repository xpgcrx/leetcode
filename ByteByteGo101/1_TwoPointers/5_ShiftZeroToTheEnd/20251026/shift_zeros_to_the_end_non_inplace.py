from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    ret = [0] * len(nums)
    idx = 0
    for n in nums:
        if n != 0:
            ret[idx] = n
            idx += 1
    return ret

