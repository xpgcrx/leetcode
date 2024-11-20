class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            l = [0] * 26
            for c in s:
                index = ord(c) - ord("a")
                l[index] += 1
            group[tuple(l)].append(s)
        return list(group.values())
