# 118-pascal's_triangle
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution:
    def generate(self, numRows):

        result = []
        if numRows > 0:
            result.append([1])

        for n in range(numRows - 1):
            newRow = [1]

            if len(result[-1]) >= 2:
                for x in range(len(result[-1]) - 1):
                    newRow.append(result[-1][x] + result[-1][x + 1])

            newRow.append(1)
            result.append(newRow)

        return result
