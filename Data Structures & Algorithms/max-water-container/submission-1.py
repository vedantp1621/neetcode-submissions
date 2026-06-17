class Solution:
    def maxArea(self, heights: List[int]) -> int:
        containers = [] # we will push all the calculated containers here and return
                        # the max one
        left, right = 0, len(heights) - 1 # initialize far left and far right pointers
        while left < right: # standard two pointers loop. All we need to do here is 
                            # move the pointer that has the lesser height, since the 
                            # entire rectangle area depends on the lesser one. This
                            # allows us to only check the best permutations
            if heights[right] < heights[left]: # if right is less, move right <-
                containers.append((right - left) * (heights[right])) # add the container
                                                                     # created by this 
                                                                     # permutation
                right -= 1
            else: # left is less so move left ->
                containers.append((right - left) * (heights[left])) # add the container
                                                                     # created by this 
                                                                     # permutation
                left += 1
            
        return max(containers) # return the greatest permutation


