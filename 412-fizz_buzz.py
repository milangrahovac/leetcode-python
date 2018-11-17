# 412. Fizz Buzz
#
# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number
# and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.


class Solution(object):
    def fizzBuzz(self, n):

        result = []

        for x in range(1, n+1):
            if x % 15 == 0:
                x = "FizzBuzz"
            elif x % 5 == 0:
                x = "Buzz"
            elif x % 3 == 0:
                x = "Fizz"
            result.append(str(x))
        return result
