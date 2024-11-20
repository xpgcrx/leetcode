class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Group anagrams from the input array of strings.

        Time Complexity: O(N * K * log K)
            - N is the length of input array strs
            - K is the length of the longest string
            - Sorting each string takes O(K * log K), done N times

        Space Complexity: O(N * K)
            - N is the length of input array strs
            - K is the length of the longest string
            - Need to store all strings in hashmap and sorted tuples

        Args:
            strs: List of strings to be grouped

        Returns:
            List of lists where each inner list contains anagrams
        """
        group = defaultdict(list)
        for s in strs:
            sorted_list = sorted(s)
            group[tuple(sorted_list)].append(s)

        return list(group.values())
