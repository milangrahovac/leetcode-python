# 844. Backspace String Compare
#
# Given two strings S and T, return if they are equal when both are typed into empty text editors.
# # means a backspace character.
#
# Example 1:
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
#
# Example 2:
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
#
# Example 3:
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
#
# Example 4:
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
#
# Note:
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.


class Solution:
    def backspaceCompare(self, S, T):

        s = backspace(S)
        t = backspace(T)

        return s == t


def backspace(word):
    new_word = ""
    for x in word:
        if x != "#":
            new_word += x
        else:
            new_word = new_word[:-1]
    return new_word
