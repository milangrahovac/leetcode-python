# 824. Goat Latin
#
# A sentence S is given, composed of words separated by spaces.
# Each word consists of lowercase and uppercase letters only.
# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
#
# The rules of Goat Latin are as follows:
# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
# For example, the word 'apple' becomes 'applema'.
#
# If a word begins with a consonant (i.e. not a vowel), 
# remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
#
# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, 
# the second word gets "aa" added to the end and so on.
# Return the final sentence representing the conversion from S to Goat Latin.
#
#
# Example 1:
# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
#
# Example 2:
# Input: "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


class Solution:
    def toGoatLatin(self, S):

        s = S.split(" ")
        vowels = ["a", "e", "i", "o", "u"]
        result = []

        for x in range(len(s)):
            word = s[x]
            if word[0].lower() not in vowels:
                if len(word) > 1:
                    word = word[1:] + word[:1]

            word += "ma" + ("a" * (x+1))
            result.append(word)

        return " ".join(result)
