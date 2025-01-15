"""
Given an array nums of distinct integers, return all the possible 
permutations
. You can return the answer in any order.
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        
        result = []
        def backtrack(subset):
            # base case
            if len(subset) == len(nums):
                result.append(copy.copy(subset))
                return
            # recursive case
            else:
                for num in nums:
                    if num in subset:
                        continue
                    subset.append(num)
                    backtrack(subset)
                    subset.pop()
            
        backtrack([])
        return result
