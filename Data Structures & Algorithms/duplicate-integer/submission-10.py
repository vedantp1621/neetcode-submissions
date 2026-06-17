class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        nums_s = set(nums)
        return len(nums_s) < len(nums)
