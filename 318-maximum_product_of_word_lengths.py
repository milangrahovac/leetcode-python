# 318-maximum_product_of_word_lengths
#
# Given a string array words,
# find the maximum value of length(word[i]) * length(word[j])
# where the two words do not share common letters.
# You may assume that each word will contain only lower case letters.
# If no such two words exist, return 0.
#
# Example 1:
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
#
# Example 2:
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
#
# Example 3:
# Input: ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.


class Solution(object):
    def maxProduct(self, words):

        result = 0
        setedList = []

        for x in range(len(words)):
            setedList.append(set(words[x]))

        for x in range(len(setedList)):
            for y in range(x+1, len(setedList)):
                if not any(letter in setedList[y] for letter in setedList[x]):
                    result = max(result, len(words[x]) * len(words[y]))

        return result
