class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set() # use a set because sets keep only unique values
        for num in nums: # iterate through each num
            unique.add(num) # adding duplicates is not allowed in sets
        return len(unique) != len(nums) # if there are duplicates, this will return true

         