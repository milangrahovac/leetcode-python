# 242. Valid Anagram
#
# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution(object):
    def isAnagram(self, s, t):

        checked_letters = []

        if len(s) == 0 and len(t) == 0:
            return True

        if len(s) == len(t):
            for x in s:
                if len(s) == len(t):
                    if x not in checked_letters:
                        if x in t:
                            s = s.replace(x, "")
                            t = t.replace(x, "")
                            checked_letters.append(x)

                            if len(s) == 0 and len(t) == 0:
                                return True
            return False
        else:
            return False
