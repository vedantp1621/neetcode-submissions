class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open paranthesis sif open < n
        #only add a closing parenthesis if closed < open
        #valid if open == close == n

        stack = []
        results = []

        # recursive function
        def backtrack(numOpen, numClosed):
            if numOpen == numClosed == n: # no more opens can be added, and all closed
                                          # caught up with the opens
                results.append("".join(stack)) # takes all elements in stack and joins 
                                           # them into one string
                return # end this recursive branch

            if numOpen < n: # more opens can be added
                stack.append("(") # add open
                backtrack(numOpen + 1, numClosed) # recurse with an additional open
                stack.pop() # once branch ends, return up the stack by popping
            
            if numClosed < numOpen: # more closed can be added
                stack.append(")") # add closed
                backtrack(numOpen, numClosed + 1) # recurse with additional closed
                stack.pop() # once branch ends, return up the stack by popping

        backtrack(0,0) # starts the recursion 
        return results # return the final array. Elements in this array are added as the
                   # stack gets propegated up (when we pop). Before popping, the backtrack
                   # function must return, so it must add that branch's combination of closed
                   # and opens