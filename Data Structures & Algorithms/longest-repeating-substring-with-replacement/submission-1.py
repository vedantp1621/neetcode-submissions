class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # initialize a dict to track key:value pairs
                   # letter:count
        res = 0 # initialize the tracker to mark the largest window size
        l = 0 # start the left poiinter at 0, we will be pulling r -> until the 
              # window no longer fits the specifications

        for r in range(len(s)): # pull the r ->, expanding the window until it reaches
                                # its end
            count[s[r]] = 1 + count.get(s[r], 0) # incremenet the count of the current
                                                 # letter by 1

            while (r-l+1) - max(count.values()) > k: # checks if the widnow does not
                                                     # fit the specificatioms. 
            # Essentially, if the length of the window - the highest occuring letter
            # exceeds the # of replacements we have, we cannot make a valid window.
            # therefore, we must shrink the window by moving the left pointer -> until
            # the window works again
                count[s[l]] -= 1 # remove the removed letter from the counts
                l += 1 # move l ->

            res = max(res, r-l+1) # update res by setting it as the highest recorded 
                                  # window

        return res # return the highest recorded window
 

