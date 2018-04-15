# 80. Remove Duplicates from Sorted Array II
#
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
# It doesn't matter what you leave beyond the new length.


class Solution(object):
    def removeDuplicates(self, nums):
        for num in set(nums):
            counter = nums.count(num)

            if counter > 2:
                for x in range(0, counter-2):
                    nums.remove(num)

        return len(nums)
