class MinStack:

    '''
    ideas for min structure
    
    hashing function

    internal stack just for min
    adding:
    if the item to be added is the new min, add to stack
    eventually, this stack should contain all historic mins, with recent at top

    removing:
    if the item we remove is at the top of the stack, pop from stack and return
    the next value as the next min
    '''

    def __init__(self):
        self.struct = []
        self.minTrack = []        

    def push(self, val: int) -> None:
        if not self.struct:
            self.minTrack.append(val)
        elif val <= self.minTrack[-1]:
            self.minTrack.append(val)

        self.struct.append(val)
        
    def pop(self) -> None:
        if self.struct[-1] == self.minTrack[-1]:
            self.minTrack.pop()
        
        self.struct.pop(-1)

    def top(self) -> int:
        return self.struct[-1]

    def getMin(self) -> int:
        return self.minTrack[-1]
