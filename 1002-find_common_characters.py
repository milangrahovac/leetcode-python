# 1002. Find Common Characters


# Given an array A of strings made only from lowercase letters, 
# return a list of all characters that show up in all strings within the list (including duplicates).  
# For example, if a character occurs 3 times in all strings but not 4 times, 
# you need to include that character three times in the final answer.
# You may return the answer in any order.

# Example 1:

# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: ["cool","lock","cook"]
# Output: ["c","o"]
 

# Note:

# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter


class Solution(object):
    def commonChars(self, A):

        result = []
        a = list(set(A))

        for letter in set(list(a[0])):
            n = a[0].count(letter)

            for i in range(1, len(a)):
                n = min(n, a[i].count(letter))
                if n == 0:
                    break

            if n > 0:
                for x in range(n):
                    result.append(letter)

        return result
