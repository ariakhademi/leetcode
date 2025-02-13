"""
Given an integer array nums and an integer k, 
return true if there are two distinct indices 
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        container = {}
        for i, num in enumerate(nums):
            if nums[i] in container and abs(i - container[num]) <= k:
                return True
            container[num] = i
        return False
        