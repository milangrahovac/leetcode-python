# 137. Single Number II
#
# Given an array of integers, every element appears three times except for one,
# which appears exactly once. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?


class Solution(object):
    def singleNumber(self, nums):

        nums = sorted(nums)

        for x in range(0, len(nums), 3):
            if x != len(nums) - 1:

                if nums[x] != nums[x + 1] and nums[x] != nums[x + 2]:
                    return nums[x]
            else:
                return nums[x]
