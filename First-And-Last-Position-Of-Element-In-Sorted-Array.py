class Solution:
    def binary_search(self, nums, target, left):
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                high = mid
            else:
                low = mid + 1
        return low

    def searchRange(self, nums, target):
        # Brute Force --> O(n)
        #         min = -1
        #         max = -1
        #         for i in range(len(nums)):
        #             if nums[i] == target:
        #                 if min == -1:
        #                     min = i
        #                 else:
        #                     max = i
        #         return [min, max]

        # Modified Binary Search (see above method) --> Time O(logn), Space O(1)
        start = self.binary_search(nums, target, True)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, self.binary_search(nums, target, False) - 1]

def main():
    solve = Solution()
    print(solve.searchRange([5,7,7,8,8,10], 8))

if __name__ == '__main__':
    main()



