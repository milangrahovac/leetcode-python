# 14. Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        else:
            sorted_strs = sorted(strs, key=len)
            shortest_word = sorted_strs[0]

            for x in range(len(shortest_word), -1, -1):
                prefix = shortest_word[:x]

                if all(word.startswith(prefix) for word in strs):
                    return prefix
