# 438. Find All Anagrams in a String
#
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Example 2:
#
# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".



import collections

class Solution(object):
    def findAnagrams(self, s, p):

        pc = collections.Counter(p)
        slice_str = s[:len(p)]
        sc = collections.Counter(slice_str)

        slice_index = []

        for x in range(0, len(s) - len(p) + 1):
            if x > 0:
                sc[s[x-1]] -= 1
                sc[s[x+len(p)-1]] += 1

                if sc[s[x-1]] == 0:
                    del sc[s[x-1]]

            if len(sc) == len(pc):
                if sc == pc:
                    slice_index.append(x)

        return slice_index
