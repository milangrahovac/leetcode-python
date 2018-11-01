# 047_permutations_2

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
#
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


from itertools import permutations


class Solution:
    def permuteUnique(self, nums):
        p = list(permutations(nums, len(nums)))
        result = []
        for x in p:
            if list(x) not in result:
                result.append(list(x))
        return result
