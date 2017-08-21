# 268. Missing Number
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# For example,
# Given nums = [0, 1, 3] return 2.
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?



class Solution(object):
    def missingNumber(self, nums):

        if len(nums) > 1:

            real_sum = sum(nums)
            expected_sum = 0
            max_num = max(nums)

            for x in range(len(nums)):
                expected_sum += x

            if real_sum > expected_sum:
                missing_num = max_num - (real_sum - expected_sum)
                return missing_num
            elif real_sum < expected_sum:
                missing_num = expected_sum - real_sum
                return missing_num
            else:
                return max_num+1

        else:
            if nums[0] == 0:
                return 1
            else:
                return 0
