# 504. Base 7
#
# Given an integer, return its base 7 string representation.
#
# Example 1:
# Input: 100
# Output: "202"
#
# Example 2:
# Input: -7
# Output: "-10"
#
# Note: The input will be in range of [-1e7, 1e7].


class Solution:
    def convertToBase7(self, num):

        if num == 0:
            return "0"

        result = ""
        n = abs(num)

        while n > 0:
            x = n % 7
            n = int(n / 7)
            result = str(x) + result

        return result if num > 0 else "-" + result
