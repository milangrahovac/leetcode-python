# 13. Roman to Integer
#
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.


roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Solution(object):
    def romanToInt(self, s):
        num_list = []
        int_num = 0

        for x in range(0, len(s)):
            if s[x] in roman:
                num_list.append(roman[s[x]])

        for m in range(0, len(num_list)-1):
            if num_list[m] >= num_list[m+1]:
                int_num += num_list[m]
            else:
                int_num -= num_list[m]

        int_num += num_list[len(num_list)-1]
        return int_num
