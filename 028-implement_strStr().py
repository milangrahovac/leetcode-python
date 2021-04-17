# 28. Implement strStr()
#
# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1


class Solution:
    def strStr(self, haystack, needle):

        if haystack == needle or len(needle) == 0:
            return 0
        if needle in haystack:
            for x in range(len(haystack) - len(needle) + 1):
                if haystack[x] == needle[0]:
                    if needle == haystack[x : x + len(needle)]:
                        return x

        return -1
