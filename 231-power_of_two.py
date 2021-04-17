# 231. Power of Two
#
# Given an integer, write a function to determine if it is a power of two.


class Solution(object):
    def isPowerOfTwo(self, n):

        power_of_two = 2

        if n in [1, 2]:
            return True
        else:
            while n > power_of_two:
                power_of_two *= 2
                if n == power_of_two:
                    return True
            return False
