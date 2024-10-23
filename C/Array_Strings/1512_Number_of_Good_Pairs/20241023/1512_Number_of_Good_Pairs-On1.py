# O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)  # 要素ごとの出現回数を記録
        count = 0

        for num in nums:
            count += freq[
                num
            ]  # すでにこの要素が出現していた回数分だけペアが作れる
            freq[num] += 1  # この要素の出現回数を更新

        return count
