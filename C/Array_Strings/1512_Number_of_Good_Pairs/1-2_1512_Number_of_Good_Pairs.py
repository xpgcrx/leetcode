# O(n) Solution
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        good_pairs = 0

        for num in count:
            n = count[num]
            good_pairs += (n * (n - 1)) // 2  # nC2

        return good_pairs
