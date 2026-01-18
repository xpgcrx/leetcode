from typing import List

# r=0の特別扱いが必要になるため、真ん中のjベースは良くない→没
def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    if not nums:
        return 0
    if len(nums) < 3:
        return 0
   
    left_count = {}
    right_count = {}

    left_count[nums[0]] = 1
    for idx in range(2, len(nums)):
        right_count[nums[idx]] = right_count.get(nums[idx], 0) + 1

    ret = 0
    for j in range(1, len(nums)-1):
        if nums[j] % r == 0:
            ln = left_count.get(nums[j]//r, 0) # pythonの/は小数を生成するので整数除算の//にする
            rn = right_count.get(nums[j]*r, 0)
            ret += ln * rn

        # for next loop
        if nums[j] in left_count:
            left_count[nums[j]] += 1
        else:
            left_count[nums[j]] = 1

        if nums[j+1] in right_count:
            right_count[nums[j+1]] -= 1
    return ret

