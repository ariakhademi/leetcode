"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            raise Exception('Empy input')
            return [0]

        my_dictionary = {}

        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in my_dictionary:
                return [my_dictionary[remaining],i]
            else:
                my_dictionary[nums[i]] = i