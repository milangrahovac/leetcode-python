# Given a List of words, return the words that can be typed using letters of alphabet
# on only one row's of American keyboard like the image below.
# Example 1:
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
#
# Note:
#
# 1. You may use one character in the keyboard more than once.
# 2. You may assume the input string will only contain letters of alphabet.


class Solution(object):
    def findWords(self, words):
        row1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        row2 = ["A", "S", "D", "F", "G", "H","J", "K", "L", "a", "s", "d", "f", "g", "h","j", "k", "l"]
        row3 = ["Z", "X", "C", "V", "B", "N", "M", "z", "x", "c", "v", "b", "n", "m"]
        one_row_words = []

        for word in words:
            listed_word = list(word)
            if set(listed_word).issubset(set(row1))\
                or set(listed_word).issubset(set(row2))\
                    or set(listed_word).issubset(set(row3)):
                        one_row_words.append(''.join(listed_word))
        print(one_row_words)
        return one_row_words
