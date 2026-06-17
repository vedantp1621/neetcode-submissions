class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # init a set: unordered set of integers, does not support duplicates, 0(1) search
        l = 0 # initialize the left side of the window
        res = 0 # initialize the variable to track the biggest window size in the string
        for r in range(len(s)): # the right pointer will constantly move right through this loop
                                # the only time it will stop, is if a dupe is detected, in which case
                                # the left pointer will be allowed to catch up until the dupe is gone. 
                                # This is the pointer logic here
                                
            while s[r] in charSet: # 2) Duplicate found, now we must let left close the window until the duplicate
                                   #    is gone. Then, we start the next window at the point right after the prev
                                   #    duplicate. 
                charSet.remove(s[l])
                l += 1
            #1) No duplicate found yet, expand window further and add letter to current window's hash set. Update
            #   the max value if its bigger.
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res # return the final recorded highest size