"""
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_length = 0

        for num in my_set:
            seq_length = 1
            if (num - 1) not in my_set:
                current_num = num
                while (current_num + 1) in my_set:
                    seq_length += 1
                    current_num += 1

                max_length = max(max_length,seq_length)

        return max_length