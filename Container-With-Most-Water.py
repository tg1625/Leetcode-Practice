"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
 n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
  Find two lines, which together with x-axis forms a container, such that the container contains the most water.

https://leetcode.com/problems/container-with-most-water/
"""


class Solution:
    def maxArea(self, height):
        # Brute Force -->Time O(n^2), Space O(1)
        # max_area = 0
        # for num1 in range(len(height)):
        #     for num2 in range(1, len(height)):
        #         if (num2 - num1)*min(height[num1], height[num2]) >= max_area:
        #             max_area = (num2 - num1)*min(height[num1], height[num2])
        # return max_area

        # Two Pointers --> Time O(n), Space O(1)
        max_area = 0
        left = 0
        right = len(height) - 1
        while (left < right):
            max_area = max(max_area, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


def main():
    solve = Solution()
    print(solve.maxArea([1,8,6,2,5,4,8,3,7]))

if __name__ == '__main__':
    main()
