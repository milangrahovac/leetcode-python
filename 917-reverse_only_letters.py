# 917 - reverse only letters
#
# Given a string S, return the "reversed" string where all characters
# that are not a letter stay in the same place, and all letters reverse their positions.
#
# Example 1:
# Input: "ab-cd"
# Output: "dc-ba"
#
# Example 2:
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#
# Example 3:
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
# Note:
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S doesn't contain \ or "


from string import ascii_letters


class Solution:
    def reverseOnlyLetters(self, S):

        string = ""

        for x in range(len(S)):
            if S[x] in ascii_letters:
                string += S[x]

        string = list(string[::-1])

        for x in range(len(S)):
            if S[x] not in ascii_letters:
                string.insert(x, S[x])

        return "".join(string)
