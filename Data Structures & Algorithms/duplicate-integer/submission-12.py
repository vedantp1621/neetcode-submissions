class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        nums_set = set(nums) #temp
        return len(nums_set) < len(nums)
