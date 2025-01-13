class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = defaultdict(int)
        dt = defaultdict(int)

        for c in s:
            ds[c] += 1
        for c in t:
            dt[c] += 1

        return ds == dt
