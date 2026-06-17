class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # you can treat the value that we want to search for as the 'min'
        # start left at far left
        # start right at far right
        # if left is > mid, we know that left side is larger sorted section
        # else, right is larger sorted section
        # 

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]: # left subsec smaller
                if nums[l] <= target < nums[m]: 
                    r = m - 1
                else: 
                    l = m + 1
            else: # left subsec greater
                if nums[m] < target <= nums[r]: 
                    l = m + 1
                else: 
                    r = m - 1
        return -1

        
