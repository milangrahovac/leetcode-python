# 26. Remove Duplicates from Sorted Array
#
#  Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeDuplicates(self, nums):

        if len(nums) <= 1:
            return len(nums)
        else:

            start = 0

            for x in range(1, len(nums)):
                if nums[start] != nums[x]:
                    start += 1
                    nums[start] = nums[x]

        return start + 1
