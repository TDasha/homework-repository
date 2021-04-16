"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    maximal_subarr_sum = nums[0]
    end = k
    max_sum_list = []

    for start in range(len(nums) - k + 1):
        max_sum = 0
        sorted_nums = sorted(nums[start:end], reverse=True)
        for item in sorted_nums:
            max_sum += item
            max_sum_list.append(max_sum)
        end += 1

    for item in max_sum_list:
        if item > maximal_subarr_sum:
            maximal_subarr_sum = item

    return maximal_subarr_sum
