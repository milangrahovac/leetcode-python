# 462. Minimum Moves to Equal Array Elements II



# Given a non-empty integer array, find the minimum number of moves 
# required to make all array elements equal, 
# where a move is incrementing a selected element by 1 
# or decrementing a selected element by 1.

# You may assume the array's length is at most 10,000.

# Example:
# Input:
# [1,2,3]
# Output:
# 2

# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]



from statistics import median

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        result = 0
        m = int(median(nums))
        
        for x in nums:
            if x > m:
                result += x-m
            elif x < m:
                result += m-x
        
        return result
        