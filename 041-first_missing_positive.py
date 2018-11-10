# 41. First Missing Positive
#
# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.


class Solution(object):
    def firstMissingPositive(self, nums):

        nums = list(set(nums))

        if len(nums) == 0:
            return 1
        elif len(nums) == 1:
            if nums[0] != 1:
                return 1
            else:
                return 2
        else:
            for x in range(1, max(nums)+2):
                if x not in nums:
                    return x

