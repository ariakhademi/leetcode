'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        # if array has only one element or array is sorted
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[middle + 1]:
                return nums[middle + 1]
            if nums[middle] < nums[middle - 1]:
                return nums[middle]
            if nums[middle] > nums[0]:
                left = middle +1
            else:
                right = middle - 1
        return nums[left]