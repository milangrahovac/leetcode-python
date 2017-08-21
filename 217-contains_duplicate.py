# 217. Contains Duplicate
#
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.


class Solution(object):
    def containsDuplicate(self, nums):

        nums = sorted(nums)

        for x in range(0, len(nums)):
            if x != len(nums) - 1:
                if nums[x] == nums[x+1]:
                    return True

        return False
