# 258. Add Digits

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.

# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?


class Solution(object):
    def addDigits(self, num):
        if len(str(num)) == 1:
            return num
        else:
            while len(str(num)) > 1:
                num1 = 0
                for x in str(num):
                    num1 += int(x)
                num = num1
            return num
