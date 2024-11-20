class Solution:
    # Time Complexity: O(NM) (N=len(strs), M = max length of each string)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                index = ord(c) - ord("a")
                counter[index] += 1
            group[tuple(counter)].append(s)

        return list(group.values())
