
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # NOTE: if you initialize an array with placeholder values, 
                                      # and a set size, the insertion costs 0(1) time
        stack = []  # pair: [temp(value), index]

        for i, t in enumerate(temperatures): # iterate through stack
                                             # returns pairs of (temp(value), index)
            while stack and t > stack[-1][0]: # while the stack is nonempty and the top
                                              # is less than the current iter (means we
                                              # will 'kill' the top of the stack) 
                stackT, stackInd = stack.pop() # stackT = tops value
                                               # stackInd = tops index
                res[stackInd] = i - stackInd # since we saved the index of the element
                                             # in the original array, all we have to do
                                             # is update that index in the final array
                                             # with the current iter - the number killed
            stack.append((t, i)) # otherwise, we simply add to the stack since the top
                                 # is greater than the iter
        return res



        # temps: [30,38,30,36,35,40,28]
        #                        __
        # stack: [40:5, 28:6   ]
        
        # final: [1 ,4 ,1 ,2 ,1 ,0 ,0 ]

