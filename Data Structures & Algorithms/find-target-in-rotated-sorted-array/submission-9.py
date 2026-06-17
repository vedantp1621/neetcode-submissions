# Tricker solution

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1 # inititalize pointers far left and far right

        while left <= right: # stop once the pointers surpass each other
            middle = left + (right-left)//2 # typical middle pointer formula
            
            if target == nums[middle]: # close loop if the target is the same as the middle
                                       # pointer, means we have the index
                return middle

            # preliminary checks are done. Due the context of the rotation, the pinchpoint
            # is only two values. Therefore, there is always one half that is sorted. We
            # will take advantage of this, find the side thats sorted, and then use that to
            # pinpoint about where the target is. Using the sorted side, we can compare the 
            # target to the left and rights of the half, figuring out if the target is in that
            # half, or the next half
            if nums[left] <= nums[middle]: # check if the left side is sorted 

                if target > nums[middle] or target < nums[left]: # check if the target is on
                                                                 # the other half (see how 
                                                                 # knowing if this half is
                                                                 # sorted allows us to do 
                                                                 # this)
                    left = middle + 1 # cut this half out
                else: # cut the other half out
                    right = middle - 1

            else: # check if the right side is sorted
                
                if target < nums[middle] or target > nums[right]:  # check if the target is on
                                                                 # the other half (see how 
                                                                 # knowing if this half is
                                                                 # sorted allows us to do 
                                                                 # this)
                    right = middle - 1 # cut this half out
                else: # cut the other half out
                    left = middle + 1 
            
        return -1 # loop ended and middle was never equallign the target
