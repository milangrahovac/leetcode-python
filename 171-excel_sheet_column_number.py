# 171. Excel Sheet Column Number

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...

# Example 1:
# Input: "A"
# Output: 1

# Example 2:
# Input: "AB"
# Output: 28

# Example 3:
# Input: "ZY"
# Output: 701


class Solution:
    def titleToNumber(self, s):
        alpha = string.ascii_uppercase
        result = 0
        
        if len(s) == 1:
            result = alpha.index(s)
        else: 
            for x in range(1, len(s)):
                result += 26 ** x
            
            while len(s) > 1:
                for i in range(1, len(s)+1):
                    result += alpha.index(s[0]) * (26 ** (len(s)-1))
                    s = s[1:]
        
        return result + 1
