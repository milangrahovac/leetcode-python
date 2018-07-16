# 506. Relative Ranks
#
# Given scores of N athletes, find their relative ranks and the people
# with the top three highest scores, who will be awarded medals:
# "Gold Medal", "Silver Medal" and "Bronze Medal".
#
# Example 1:
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores,
# so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
# For the left two athletes, you just need to output their relative ranks according to their scores.
#
# Note:
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.


class Solution:
    def findRelativeRanks(self, nums):

        sorted_nums = sorted(nums, reverse=True)

        for x in range(len(sorted_nums)):
            if x == 0:
                nums[nums.index(sorted_nums[x])] = "Gold Medal"
            elif x == 1:
                nums[nums.index(sorted_nums[x])] = "Silver Medal"
            elif x == 2:
                nums[nums.index(sorted_nums[x])] = "Bronze Medal"
            else:
                nums[nums.index(sorted_nums[x])] = str(x + 1)

        return nums
