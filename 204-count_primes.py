# 204. Count Primes

# Count the number of prime numbers less than a non-negative number, n.

# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution:
    def countPrimes(self, n: int) -> int:
        noprimes = set(j for i in range(2, int(n / 2) + 1) for j in range(i * 2, n, i))
        primes = [x for x in range(2, n) if x not in noprimes]
        return len(primes)
