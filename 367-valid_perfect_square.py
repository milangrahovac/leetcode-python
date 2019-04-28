#  367. Valid Perfect Square
#
# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
# Input: 16
# Returns: True
#
# Example 2:
# Input: 14
# Returns: False


class Solution(object):
    def isPerfectSquare(self, num):

        len_sqr = len(str(num))

        if len_sqr >= 1:

            min_root = 1
            max_root = "9"

            if len_sqr % 2 == 0:
                min_len_sqr_root = int(len_sqr / 2)
            else:
                min_len_sqr_root = int((len_sqr + 1) / 2)

            max_len_sqr_root = min_len_sqr_root + 1


            for x in range(min_len_sqr_root - 1):
                min_root *= 10

            for i in range(max_len_sqr_root - 2):
                max_root += "9"

            max_root = int(max_root)

            for s in range(min_root, max_root):
                if s * s == num:
                    return True
            return False
