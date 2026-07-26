class MinStack:
# purpose of this class: stack functionality that supports push, pop, top
# should always push minimum to top, so we must keep a running min tracker

# to do everything in 0(1), we need some global benchmark and store differences from the global bench
# we will make that the first value

    def __init__(self):
        self.min = float('inf') # running min
        self.stack = [] # overall stack
        
    def push(self, val: int) -> None: # we are essentially storing differences from min, and 
                                      # keeping running minimum 
        if not self.stack: # if there is no value, make first val the min and add 0 to the stack
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val-self.min) # append the difference from the val to the min
            if val < self.min:
                self.min = val
        
    def pop(self) -> None:
        if not self.stack:
            return # if the stack doesnt exist or is empty, do nothing

        stack_diff = self.stack.pop() # get the current difference

        if stack_diff < 0: # if the diff is
            self.min = self.min - stack_diff 

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min


    def getMin(self) -> int:
        return self.min
        
