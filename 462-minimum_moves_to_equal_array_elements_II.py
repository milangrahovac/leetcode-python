462. Minimum Moves to Equal Array Elements II


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
        