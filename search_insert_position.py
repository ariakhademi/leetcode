class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while(left <= right):
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle # found
            elif target > nums[middle]:
                left = middle + 1 # narrow down to left
            else:
                right = middle - 1 # narrow down to right
        
        # if target is not in list
        return left