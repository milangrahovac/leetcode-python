# 674. Longest Continuous Increasing Subsequence
#
# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
#
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
#
# Note: Length of the array will not exceed 10,000.


class Solution:
    def findLengthOfLCIS(self, nums):
        if len(nums) == 0:
            return 0
        result, n = 0, 1
        for x in range(len(nums)-1):
            if nums[x] < nums[x+1]:
                n += 1
            else:
                result = max(result, n)
                n = 1
        return max(result, n)
