from typing import List

def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    if not nums:
        return 0
    nums_set = set(nums)
    ret = 1
    for num in nums:
        longest = 1
        target = num + 1
        while target in nums_set:
            longest += 1
            target += 1
        ret = max(ret, longest)
    return ret
            
