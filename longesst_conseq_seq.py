"""
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = []
        i = 0

        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        if all(x == nums[0] for x in nums):
            return 1

        while i < len(nums):
            if (nums[i] + 1) in nums:
                out.append(nums[i])
                i = nums.index(nums[i] + 1)
            elif len(out) > 0:
                out.append(nums[i])
                break
            elif not out:
                i += 1
            else: 
                break
        
        return len(out)
        