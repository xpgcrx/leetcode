from typing import List


def triplet_sum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []

    nums = sorted(nums)
    s = set()
    for i in range(0, len(nums) - 2):
        a = nums[i]

        if 0 < a:
            break

        # avoid duplicated 'a'
        if 0 < i and nums[i - 1] == nums[i]:
            continue

        left = i + 1
        right = len(nums) - 1
        target = -a
        while left < right:
            b = nums[left]
            c = nums[right]
            sum = b + c
            if sum == target:
                s.add((a, b, c))
                left += 1
            elif sum < target:
                left += 1
            else:
                right -= 1
    return [list(t) for t in s]
