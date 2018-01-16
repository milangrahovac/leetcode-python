# 49. Group Anagrams
#
# Given an array of strings, group anagrams together.
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
# Note: All inputs will be in lower-case.



import collections
class Solution:

    def groupAnagrams(self, strs):

        result = []
        dic = collections.defaultdict(list)

        for s in strs:
            dic[str(sorted(s))].append(s)

        for value in dic.values():
            result.append(value)

        return result


a = ["eat", "tea", "tan", "ate", "nat", "bat"]
b = ["eat", "abc", "acb", "tea", "", "tan", "ate", "", "nat", "bat"]


print(a, "rezultat:", Solution().groupAnagrams(a))
print(b, "rezultat:", Solution().groupAnagrams(b))
