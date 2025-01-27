class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            raise Exception('Value error: nums is empty')
            return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            if nums[middle] >= nums[left]:
                # we are within the left sorted side
                if nums[middle] > target >= nums[left]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                # we are within the right sorted side
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1