"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        for j in range(1,len(nums)+1):
            for i in range(len(nums)):
                if sum(nums[i:i+j]) >= target:
                    return len(nums[i:i+j])
        return 0