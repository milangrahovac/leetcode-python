# 728. Self Dividing Numbers
#
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# Also, a self-dividing number is not allowed to contain the digit zero.
#
# Given a lower and upper number bound, output a list of every possible self dividing number, 
# including the bounds if possible.
#
# Example 1:
# Input:
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
#
# Note:
# The boundaries of each input argument are 1 <= left <= right <= 10000.


class Solution:

    def selfDividingNumbers(self, left, right):

        nums = list(range(left, right+1))
        result = []
        num_is_self_dividing = True

        for num in nums:
            if "0" not in str(num):

                for x in str(num):
                    if not int(num) % int(x) == 0:
                        num_is_self_dividing = False
                        break
                    num_is_self_dividing = True

                if num_is_self_dividing:
                    result.append(int(num))
        return result


print(Solution().selfDividingNumbers(4, 51))
