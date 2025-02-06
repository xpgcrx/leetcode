from typing import List


# Time: O(n + n) = O(n)
# Space: O(n)
def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    if not nums:
        return 0

    nums_set = set(nums)
    longest = 1
    for n in nums:
        if n - 1 in nums_set:
            # n isn't the smallest number in its chain.
            continue

        # If the current number is the smallest number in its chain,
        # search for the length of its chain.
        current_num = n
        current_chain = 1
        while current_num + 1 in nums_set:
            current_num += 1
            current_chain += 1
        longest = max(longest, current_chain)
    return longest
