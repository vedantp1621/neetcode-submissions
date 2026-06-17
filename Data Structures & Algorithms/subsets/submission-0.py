class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] # arr to track all permutations
        sublist = [] # arr to track this specific sublist permutation

        # decisions, either we add the num or dont add it
        def dfs(level): # recurse by level
            if level >= len(nums): # this if is only accesed at the bottom level
                                   # once all decisions have been made
                result.append(sublist.copy()) # add the sublist (all decisions made)
                                              # to results
                return # break 
            sublist.append(nums[level]) # decision to add
            dfs(level+1) # push the level down
            sublist.pop() # decision to not add 
            dfs(level+1) # push the level down
            
        dfs(0) # start the recursive stack
        return result # return the final res