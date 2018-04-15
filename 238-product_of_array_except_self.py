# 238. Product of Array Except Self
#
# Given an array of n integers where n > 1, nums, return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
# Follow up:
# Could you solve it with constant space complexity?
# (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums):

        product = 1
        result = []

        for num in nums:
            if num != 0:
                product *= num

        if 0 not in nums:
            for x in nums:
                result.append(int(product/x))
        elif nums.count(0) == 1:
            for x in nums:
                if x == 0:
                    result.append(product)
                else:
                    result.append(0)
        else:
            for x in nums:
                result.append(0)

        return result



if __name__ == '__main__':

    # test it
    a = [1, 2, 3, 4]
    b = [2, 2, 3, 4, 5, 6]

    print(a, Solution().productExceptSelf(a))
    print(b, Solution().productExceptSelf(b))
