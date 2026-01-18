from typing import List

# Time: O(n^3)
# Space: O(n^3)
def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    count_set = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] * r == nums[j] and nums[j] * r == nums[k]:
                    count_set.add((i,j,k))
    return len(count_set)


