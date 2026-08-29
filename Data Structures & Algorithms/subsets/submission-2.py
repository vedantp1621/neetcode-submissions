class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking is where you go down a treee, and then compute the reswults on the way back up
        # in this case, we can follow this
        # at each number, we have a choice: to include that number in the set or to not include it
        # for each number, we explore both choices

        res = []
        subset = []

        def dfs(i): # i is the index of the element in the list, we start with dfs of 0
            if i >= len(nums): # if the index is beyond the end of the list, we can stop
                res.append(subset.copy()) # we add whatever is in this version
                return 
            subset.append(nums[i]) # version where you add the number to the subset
            dfs(i+1) # explore this version
            subset.pop() # version where you dont add the number to the subset
            dfs(i+1) # explore this verson

        dfs(0)
        return res
