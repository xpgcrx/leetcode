class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in s:
            # n - 1が存在しないものを連続する数列の開始地点と考える
            if n - 1 not in s:
                current_num = n
                count = 1
                while current_num + 1 in s:
                    current_num += 1
                    count += 1

                longest = max(count, longest)
        return longest
