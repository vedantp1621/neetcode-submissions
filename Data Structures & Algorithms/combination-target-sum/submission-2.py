class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # we are choosing WHICH number to take next, not IF we take the next number 
        sequences = []
        run = []

        def dfs(start, remaining): # recursively process if we need this number in the combo or not

            # base case is when the currnent sum is equal to the target
            # - then we append the current sequence to the res list
            # base case is when every number was processed and that value does not equal the target
            # - then we clear the sequence and return 

            # at each step, check this:
            # - add the next number to the sequence
            # - call dfs
            # - remove that number that was just added
            # - call dfs 
            
            
            if remaining == 0: # we have a sequence that reached the target
                sequences.append(run.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(nums)):
                run.append(nums[i]) 
                dfs(i, remaining - nums[i]) # explore solution where we add this number
                run.pop() 


        dfs(0, target)
        return sequences
                

