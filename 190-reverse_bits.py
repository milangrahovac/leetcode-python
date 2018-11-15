# 190. Reverse Bits
#
# Reverse bits of a given 32 bits unsigned integer.
#
# Example:
#
# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as 00000010100101000001111010011100,
#              return 964176192 represented in binary as 00111001011110000010100101000000.
#
#


class Solution:
    def reverseBits(self, n):
        b = "{:032b}".format(n)
        return int(b[::-1], 2)
