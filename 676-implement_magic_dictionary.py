# 676. Implement Magic Dictionary
#
# Implement a magic directory with buildDict, and search methods.
# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
# For the method search, you'll be given a word, and judge whether if you modify exactly one character
# into another character in this word, the modified word is in the dictionary you just built.
#
# Example 1:
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
#
# Note:
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now.
# You could think about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class MagicDictionary,
# as static/class variables are persisted across multiple test cases. Please see here for more details.


class MagicDictionary:
    def __init__(self):
        self.__dict__ = {}

    def buildDict(self, dict):
        for item in dict:
            self.__dict__[item] = len(self.__dict__) + 1
        return self.__dict__

    def search(self, word):
        for k in self.__dict__:
            n = 0
            if len(word) == len(k):
                for i in range(len(word)):
                    if word[i] != k[i]:
                        n += 1
                    if n == 2:
                        break
                if n == 1:
                    return True
        return False
