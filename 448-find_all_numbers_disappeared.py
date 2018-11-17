# 448. Find All Numbers Disappeared in an Array
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
# some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.
# Could you do it without extra space and in O(n) runtime?
# You may assume the returned list does not count as extra space.
#
# Example:
# Input: [4,3,2,7,8,2,3,1]
# Output: [5,6]


class Solution(object):
    def findDisappearedNumbers(self, nums):

        results = []
        if type(nums) is None:
            return None
        else:
            if len(nums) == 0:
                return nums
            else:
                nums_set = set(nums)
                for x in range(1, max(max(nums_set), len(nums))+1):
                    if x not in nums_set:
                        results.append(x)
                return results
