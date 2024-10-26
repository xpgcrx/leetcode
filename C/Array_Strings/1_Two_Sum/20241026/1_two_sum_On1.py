# O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        distances = {}
        for i, num in enumerate(nums):
            if num in distances:
                return distances[num], i
            distance = target - num
            distances[distance] = i
