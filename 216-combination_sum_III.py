# 216. Combination Sum III
#
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
#
# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]


import itertools


class Solution:
    def combinationSum3(self, k, n):

        result = []

        for x in itertools.combinations(list(range(1, 10)), k):
            if sum(list(x)) == n:
                result.append(list(x))
        return result


print(Solution().combinationSum3(3, 7))
print(Solution().combinationSum3(3, 9))
