class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # integer array nums w n+1 ints (1-n)
        # one integer repeats in this array
        # we have to find it

        '''
        Brute force: iterate through the array and use a 
        hash set to track if a duplicate was found

        Optimization: 
        '''

        slow, fast = 0, 0

        while True: # this gives us the pt where the 
                    # fast and slow meet
            slow = nums[slow] # one hop in the array
            fast = nums[nums[fast]] # two hops in this array
            if slow == fast:
                break

        # Walking F steps from the meeting point arrives at the cycle entry,
        # where F = distance from index 0 to the cycle entry.
        # So if slow2 starts at 0 and slow continues from the meeting point,
        # both moving one step at a time, they converge at the cycle entry.
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
