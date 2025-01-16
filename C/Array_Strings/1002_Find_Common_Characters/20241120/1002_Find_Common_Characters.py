class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_count = defaultdict(int)
        for c in words[0]:
            min_count[c] += 1

        for word in words[1:]:
            d = defaultdict(int)
            for c in word:
                d[c] += 1

            for c, count in min_count.items():
                min_count[c] = min(count, d[c])

        ret = []
        for c, count in min_count.items():
            for i in range(count):
                ret.append(c)
        return ret
