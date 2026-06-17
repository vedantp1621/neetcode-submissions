class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures) # store res values
        stack = [] # stores [temp, index]

        for i, temp in enumerate(temperatures): # iterate through each temp
            
            while stack and temp > stack[-1][0]: # means that curr temp is > than top of stack
                
                stackTemp, stackI = stack.pop()
                res[stackI] = i - stackI

            stack.append((temp, i)) # in this case, the curr temp is not the next biggest, so we just add it to the waiting list
            # this naturally creates the index distance from the next warmer temp to any temp already in the stack

        return res