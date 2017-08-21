# 136. Single Number
#
# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution(object):
    def singleNumber(self, nums):

        nums = sorted(nums)

        for x in range(0, len(nums), 2):
            if x != len(nums) - 1:

                if nums[x] != nums[x+1]:
                    return nums[x]
            else:
                return nums[x]
