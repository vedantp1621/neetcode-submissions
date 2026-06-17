class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}            # char: frequency
        l = 0 
        res = 0
        maxfrequency = 0

        for r in range(len(s)): # right pointer embedded in loop

            # add the char
            count[s[r]] = count.get(s[r], 0) + 1 # add to the frequency of the char
            maxfrequency = max(maxfrequency, count[s[r]])

            # check if the window is now invalid, and handle
            if (r - l + 1) - maxfrequency > k: # (r-l is the old window size)
                # remove one from the left side
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res

