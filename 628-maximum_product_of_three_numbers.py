# 628. Maximum Product of Three Numbers
#
# Given an integer array, find three numbers whose product is maximum and output the maximum product.
#
# Example 1:
# Input: [1,2,3]
# Output: 6
#
# Example 2:
# Input: [1,2,3,4]
# Output: 24
#
# Note:
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.


class Solution(object):
    def maximumProduct(self, nums):

        n_product = 0
        p_product = 1
        sorter_list = sorted(nums)
        max_nums = sorter_list[-3:]

        if len(nums) >= 5:

            if sorter_list[0] < 0 and sorter_list[1] < 0:
                n_product = sorter_list[0] * sorter_list[1]

        for x in max_nums:
            p_product *= x

        if n_product != 0:

            if p_product >= n_product * max(max_nums):
                return p_product
            else:
                return n_product * max(max_nums)
        else:
            return p_product
