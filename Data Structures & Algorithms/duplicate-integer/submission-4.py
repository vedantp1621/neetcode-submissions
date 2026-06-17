class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for num in nums:
            unique.add(num)
        return len(unique) != len(nums)

         