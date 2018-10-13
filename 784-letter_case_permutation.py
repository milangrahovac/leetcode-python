# 784. Letter Case Permutation
#
# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
#
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
#
# Input: S = "12345"
# Output: ["12345"]
# 
# Note:
# S will be a string with length at most 12.
# S will consist only of letters or digits.


import itertools
import string
import collections


class Solution:
    def letterCasePermutation(self, S):

        nums = {}
        letters = ""
        result = []

        for x in range(len(S)):
            if S[x] in list(string.digits):
                nums[x] = S[x]
            else:
                letters += S[x]

        if len(letters) == 0:
            result.append(S)
        else:
            comb = list(map(list, itertools.product(*((l.upper(), l.lower()) for l in letters))))

            for c in comb:
                for n in collections.OrderedDict(sorted(nums.items())):
                    c.insert(n, nums[n])
                result.append("".join(c))

        return result
