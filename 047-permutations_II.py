# 47. Permutations II
#
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


import itertools


class Solution:
    def permuteUnique(self, nums):
        return [list(c) for c in itertools.combinations(nums, len(nums))]
