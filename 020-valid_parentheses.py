# 20. Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# The brackets must close in the correct order,
# "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution(object):
    def isValid(self, s):
        left_parentheses = ["(", "[", "{"]
        right_parentheses = [")", "]", "}"]
        parentheses_list = []
        if len(s) <= 1 or len(s) % 2 != 0:
            return False
        else:
            for x in range(len(s)):
                if s[x] in left_parentheses:
                    parentheses_list.append(s[x])
                elif s[x] in right_parentheses:
                    if len(parentheses_list) == 0:
                        return False
                    if right_parentheses.index(s[x]) == left_parentheses.index(
                        parentheses_list[-1]
                    ):
                        del parentheses_list[-1]
                    else:
                        return False
                else:
                    return False

            if len(parentheses_list) == 0:
                return True
            else:
                return False
