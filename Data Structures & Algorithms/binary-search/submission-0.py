# This problem is covered in pg. 15 of the journal

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            middle = (right-left)//2 + left

            if target > nums[middle]:
                left = middle + 1
            elif target <= nums[middle]:
                right = middle 

        return left if (left < len(nums) and nums[left] == target) else -1