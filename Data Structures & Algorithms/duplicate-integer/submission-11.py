class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        nums_se = set(nums)
        return len(nums_se) < len(nums)
