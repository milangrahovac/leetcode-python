# 229. Majority Element II
#
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Note: The algorithm should run in linear time and in O(1) space.
#
# Example 1:
# Input: [3,2,3]
# Output: [3]
#
# Example 2:
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]


class Solution(object):
    def majorityElement(self, nums):

        n = list(set(nums))
        m = int(len(nums) / 3)
        result = []

        for x in range(len(n)):
            if nums.count(n[x]) > m:
                result.append(n[x])

        return result
