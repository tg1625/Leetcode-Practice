"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums, target):
        # Brute Force --> Time O(n^2), Space O(1)
        # for num1 in range(len(nums)):
        #      for num2 in range(1, len(nums) - 1):
        #         if nums[num1] + nums[num2] == target:
        #             return [num1, num2]
        #         print(nums[num1], nums[num2 + 1])
        # return []

        # Hash Table --> Time O(n), Space O(n)
        # dict = {}
        # for num in range (len(nums)):
        #     dict[nums[num]] = num
        # for num in dict:
        #     if target - num in dict:
        #         return[dict[num], dict[target-num]]
        # return []

        # Hash Table Pt 2 --> Time O(n), Space O(n)
        # better than first b/c its n and not 2n
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [i, dict[target - nums[i]]]
            dict[nums[i]] = i
        return []

def main():
    solve = Solution()
    print(solve.twoSum([2,7,11,9], 9))


if __name__ == '__main__':
    main()



