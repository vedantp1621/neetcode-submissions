class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # to see if a char is duplicate -> use a hash set
        # to track the substring -> use a sliding window
        # to track largest window -> keep a max int

        # growing phase, when we are encountering new chars
        # shrinking phase, when we found our duplicate, clear set and reset l to r

        l = 0
        visited = set()
        max_substr = 0

        for r in range(len(s)): # until the right pointer exceeds the string window
            # shrink phase
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            # grow otherwise
            visited.add(s[r])
            max_substr = max(max_substr, r - l + 1)

        return max_substr

            


        