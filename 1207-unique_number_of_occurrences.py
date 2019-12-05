# 1207. Unique Number of Occurrences

class Solution(object):
    def uniqueOccurrences(self, arr):
        c, l = None, []
        for x in set(arr):
            c = arr.count(x)
            if c not in l:
                l.append(c)
            else:
                return False
        return True
