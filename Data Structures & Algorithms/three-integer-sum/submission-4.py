class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # create final array that will hold triplets
        nums.sort() # first, we must sort the array to setup two pointers effectively

        for i, a in enumerate(nums): # returns (index, value) pairs
            if a > 0: # logic: if the iter value is greater than one, we simply will not go on. Since
                      # we are only checking elements to the right of the current, to avoid duplicates, 
                      # if the current is positive we assume everthing else is positive, meaning we will
                      # never reach 0. 
                break

            if i > 0 and a == nums[i - 1]: # logic: this checks if the current number is the same as the prev, in 
                                           # which case we would ignore the value and move on. The reason we can 
                                           # ignore is because since we are processing elements to the right only, 
                                           # the duplicate number would not add any new computation and would be 
                                           # checking the same elements as the previous, leading to duplicate 
                                           # values
                continue

            l, r = i + 1, len(nums) - 1 # pointers to far left and right
            while l < r: # standard two pointers while
                threeSum = a + nums[l] + nums[r] # set up a sum using curr + farleft + farright
                if threeSum > 0: # if this is too big, we must downsize
                    r -= 1
                    continue
                elif threeSum < 0: # else if this is too small, we must upscale
                    l += 1
                    continue
                else: # otherwise, we know it equals 0, so we move inwards. This is a pattern in two pointers where
                      # you start from outside and slowly make your way towards the center to check new elements
                    res.append([a, nums[l], nums[r]]) # add the triplets
                    l += 1 # move inwards
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # check duplicates on new left
                        l += 1
                    while nums[r] == nums[r + 1] and l < r: # check duplicates on new right
                        r -= 1
                        
        return res
