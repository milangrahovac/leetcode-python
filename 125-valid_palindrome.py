125. Valid Palindrome

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
