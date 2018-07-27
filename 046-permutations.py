# 46. Permutations
#
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


import itertools


class Solution:
    def permute(self, nums):
        return [list(p) for p in itertools.permutations(nums, len(nums))]
