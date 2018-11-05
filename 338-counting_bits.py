# 338-counting_bits
#
# Given a non negative integer number num.
# For every numbers i in the range 0 ≤ i ≤ num
# calculate the number of 1's in their binary representation and return them as an array.
#
# Example 1:
# Input: 2
# Output: [0,1,1]
#
# Example 2:
# Input: 5
# Output: [0,1,1,2,1,2]


class Solution(object):
    def countBits(self, num):

        result = []

        for x in range(num + 1):
            bits = str(bin(x)).count("1")
            result.append(bits)
        return result
