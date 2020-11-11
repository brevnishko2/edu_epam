from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    return max(sum(i) for i in [nums[j : (j + k)] for j in range(0, len(nums) - k + 1)])
