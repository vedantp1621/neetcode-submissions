class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        final = []
        
        for i in range(len(nums)): #prefix traversal
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(nums[i-1] * prefix[i-1])

        for i in range(len(nums)): #suffix traversal
            reverse = len(nums) - i
            print(reverse)
            if i == 0:
                suffix.append(1)
            else:
                suffix.append(nums[reverse] * suffix[i-1])

        for i in range(len(nums)): #final traversal
            reverse = len(nums) - i - 1
            final.append(prefix[i] * suffix[reverse])

        return final

        
