# 214. Shortest Palindrome
#
# Given a string s, you are allowed to convert it to a palindrome
# by adding characters in front of it. Find and return the shortest palindrome
# you can find by performing this transformation.
#
# Example 1:
#
# Input: "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
#
# Input: "abcd"
# Output: "dcbabcd"


class Solution:
    def shortestPalindrome(self, s):

        if s == s[::-1]:
            return s

        for x in range(len(s) - 1, 0, -1):
            palindrome = s[x:][::-1] + s

            if palindrome == palindrome[::-1]:
                return palindrome
