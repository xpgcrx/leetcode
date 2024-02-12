class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2)
        # for i in range(len(nums)):
        #    for j in range(i+1, len(nums)):
        #        sum = nums[i] + nums[j]
        #        if sum == target:
        #            return [i, j]

        # O(n)
        # diffs = {}
        # for i, n in enumerate(nums):
        #    diff = target - n
        #    diffs.setdefault(diff, i)
        #    if n in diffs:
        #        if diffs[n] != i:
        #            return [diffs[n], i]

        # O(n)
        diffs = {}
        for i, n in enumerate(nums):
            diff = target - n
            if n in diffs:
                return [diffs[n], i]
            else:
                diffs[diff] = i
