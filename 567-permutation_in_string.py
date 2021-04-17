# 567. Permutation in String
#
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.
#
# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].


import collections


class Solution:
    def checkInclusion(self, s1, s2):

        if len(s2) >= len(s1):

            s1_counter = collections.Counter()
            for i in s1:
                s1_counter[i] += 1

            s2_cut_counter = collections.Counter()
            s2_cut = s2[: len(s1)]
            for i in s2_cut:
                s2_cut_counter[i] += 1

            if s1_counter == s2_cut_counter:
                return True
            else:
                for x in range(1, len(s2) - len(s1) + 1):
                    previous = s2[x - 1]
                    next = s2[x + len(s1) - 1]

                    s2_cut_counter[previous] -= 1
                    s2_cut_counter[next] += 1

                    if s2_cut_counter[previous] == 0:
                        del s2_cut_counter[previous]

                    if s1_counter == s2_cut_counter:
                        return True

        return False
