# 409. Longest Palindrome
#
# Given a string which consists of lowercase or uppercase letters,
# find the length of the longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input: "abccccdd"
# Output: 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.


class Solution:
    def longestPalindrome(self, s):

        result = 0

        for x in set(s):
            x_count = s.count(x)
            if x_count % 2 == 0:
                result += x_count
            else:
                result += x_count-1

        if len(s) > result:
            result += 1

        return result
