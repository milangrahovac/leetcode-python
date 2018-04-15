# 169. Majority Element
#
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.


class Solution:
    def majorityElement(self, nums):
        for x in set(nums):
            if nums.count(x) > len(nums)/2:
                return x

a = [0, 1, 0, 3, 12, 12, 12, 5, 12, 12, 12, 6, 12, 12]
b = [0, 1, 0, 3, 5, 0, 12, 2, 4, 5, 5, 5, 5, 5, 6, 5, 5, 5, 5]

print(Solution().majorityElement(a))
print(Solution().majorityElement(b))
