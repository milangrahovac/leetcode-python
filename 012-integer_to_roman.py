# 12. Integer to Roman
#
# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def intToRoman(self, num):

        if 0 < num <= 3999:

            romans0 = ["", "I", 'II', "III", "IV", "V", "VI", "VII", "VIII", "IX"]
            romans1 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
            romans2 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
            romans3 = ["", "M", "MM", "MMM"]

            num_str = str(num)
            result = ""
            n = 0

            for x in range(len(num_str) -1, -1, -1):
                if n == 0:
                    result = romans0[int(num_str[x])] + result
                elif n == 1:
                    result = romans1[int(num_str[x])] + result
                elif n == 2:
                    result = romans2[int(num_str[x])] + result
                elif n == 3:
                    result = romans3[int(num_str[x])] + result
                n += 1

            return result
