class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1 

        while l <= r: # use this format because we are trying to find
                      # the exact match
            m = (l + r) // 2

            if nums[m] < target:
                l = m+1

            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return -1

# use <= when you are trying to find an exact value or match
# use < when you are trying to find the first place where something changes



        