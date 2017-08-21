# 9. Palindrome Number
#
# Determine whether an integer is a palindrome. Do this without extra space.

class Solution(object):
    def isPalindrome(self, x):
        if x >= 0:
            rx = int(str(x)[::-1])
            if x == rx:
                return True
        return False
