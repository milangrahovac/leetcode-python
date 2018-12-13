# 290. Word Pattern

# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter 
# in pattern and a non-empty word in str.

# Example 1:
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true

# Example 2:
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false

# Example 4:
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false

# Notes:
# You may assume pattern contains only lowercase letters, 
# and str contains lowercase letters separated by a single space.


class Solution(object):
    def wordPattern(self, pattern, str):

        words = str.split()
        dict_letters = {}
        dict_words = {}

        if len(pattern) != len(words):
            return False
        else:
            for x in range(len(pattern)):
                if pattern[x] not in dict_letters:
                    dict_letters[pattern[x]] = [x]
                else:
                    dict_letters[pattern[x]].append(x)
                
                if words[x] not in dict_words:
                    dict_words[words[x]] = [x]
                else:
                    dict_words[words[x]].append(x)

                if dict_words[words[x]] != dict_letters[pattern[x]]:
                    return False

        return True
