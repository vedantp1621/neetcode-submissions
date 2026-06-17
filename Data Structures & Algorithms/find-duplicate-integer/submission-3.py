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

        while True: 
            slow = nums[slow] # one hop in the array
            fast = nums[nums[fast]] # two hops in this array
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
