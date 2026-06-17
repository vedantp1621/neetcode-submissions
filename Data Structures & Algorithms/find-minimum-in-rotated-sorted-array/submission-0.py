class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 # start l at the far left, r at the far right
   
        while l < r: # typical bs algo, we end once a pointer overlaps another
            m = l + (r - l) // 2 # calculate the middle of the range
            if nums[m] < nums[r]: # if the val at teh middle is < than the val at the far right
                                  # we know that the range should ignore everything -> of middle
                r = m # thus, set right to the middle point, cutting everything increasing to 
                      # the right off
            else: # otherwise we know that the stuff to the left is bigger, the min is not <- past the
                  # left pointer. We push left pointer closer to the middle to cut the big stuff off
                l = m + 1
        return nums[l] # once the pointers overlap, we cut all the big nums from the search, the   
                       # final num should be our minimum