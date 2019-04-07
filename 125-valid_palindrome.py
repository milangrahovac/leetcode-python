# 125. Valid Palindrome

# Given a string, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false


class Solution(object):
    def isPalindrome(self, s):

        new_string = ""
        alpha = string.ascii_letters
        nums = string.digits

        for x in s:
            if x in alpha:
                new_string += x.lower()
            elif x in nums:
                new_string += x

        return True if new_string == new_string[::-1] else False
