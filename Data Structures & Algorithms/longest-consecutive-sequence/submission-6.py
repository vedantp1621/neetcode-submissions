class Solution:

    # Input: nums = [2,20,4,10,3,4,5]

    # Input: nums = [0,3,2,5,4,6,1,1]

    def longestConsecutive(self, nums: List[int]) -> int:
        # first pass, identify start of each sequence and track them in an array
       
        # second pass, begin at each start pt and iterate forward

        numset = set(nums)
        longestset = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in numset:
                length = 1
                while nums[i] + length in numset:
                    length += 1
                longestset = max(length, longestset)

        return longestset

            
                



            