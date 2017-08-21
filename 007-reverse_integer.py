# 7. Reverse Integer
#
# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# Note:
# The input is assumed to be a 32-bit signed integer.
# Your function should return 0 when the reversed integer overflows.


class Solution(object):
    def reverse(self, x):
        rx = int(str(abs(x))[::-1])
        if rx > 2147483647:
            rx = 0
        if x < 0:
            rx = -rx
        return rx
