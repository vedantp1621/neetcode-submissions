# DISCLAIMER: This is one of those problems that you just have to recall from
# past memory, so note it down. The answer is non trivial

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's turtoise and hare
        # in this algo, we are going to assume the value at nums[n] points to 
        # an index (since all values are between 1 and n)
        # this is why we decide to use tortoise and hare. By having each elements 
        # value equal an index, we know there will be a loop somewhere if we have 
        # duplicates
        slow, fast = 0, 0 # init fast and slow pointers
        while True: # this loop ends once the cycle is found, it does not
                    # necessarily find the duplicate point
            slow = nums[slow] # change pointer to index based on what value is
                              # in the current node
            fast = nums[nums[fast]] # do the a same thing, but one step ahead
                                    # (will move twice as fast)
            if slow == fast: # once the two pointers are the same, a cycle is
                             # found
                break

        slow2 = 0 # start a new pointer at the beginning
        while True: # this is not obvious but: the distance from start to 
                    # cycle entrance (I.e duplicate #) is equal to the meeting
                    # point of slow and fast to the cycle entrance. So if we move
                    # slow and slow2 at the same pace, they will meet in the 
                    # middle at the cycle entrance
            slow = nums[slow] # move at one step per iteration
            slow2 = nums[slow2] # move at one step per iteration
            if slow == slow2: # if they meet, it HAS to be the cycle entrance
                return slow