"""
704. Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to
search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    @staticmethod
    def search(nums, target):

        low = 0
        high = len(nums) - 1

        while low <= high:
            middle = int((low + high) / 2)
            guess = nums[middle]
            if guess == target:
                return middle
            if guess > target:
                high = middle - 1
            else:
                low = middle + 1
        return -1


example = Solution()

my_list = [-1, 0, 3, 5, 9, 12]

print(example.search(my_list, 9))
