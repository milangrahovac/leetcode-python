# 387. First Unique Character in a String
#
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
# Note: You may assume the string contain only lowercase letters.


class Solution(object):
    def firstUniqChar(self, s):
        edit_list = list(s)
        newlist = list(s)
        checked_letters = []
        for x in range(len(newlist)):
            edit_list.remove(newlist[x])
            if len(checked_letters) == 26:
                return -1
            else:
                if newlist[x] not in checked_letters:
                    checked_letters.append(newlist[x])

                    if newlist[x] not in edit_list:
                        return x
                    else:
                        edit_list.append(newlist[x])
        return -1
