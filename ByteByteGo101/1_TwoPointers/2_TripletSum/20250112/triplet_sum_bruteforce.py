from typing import List


# Time: O(n^3)
# Space: O(n^2)
def triplet_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    l = len(nums)
    ret_set = set()
    for i in range(l):
        for j in range(i + 1, l):
            for k in range(j + 1, l):
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    ret_set.add((nums[i], nums[j], nums[k]))
    return [list(s) for s in ret_set]
