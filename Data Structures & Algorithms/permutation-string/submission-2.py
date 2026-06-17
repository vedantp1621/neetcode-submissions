class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # how to check the permutation: use a dict with char:frequency
        '''
        Brute force: loop through each char in s2. For each, loop forward and compare 
            each char in s1 to each next char in s2 until len(s1)

        Optimization: use two pointers. Left pointer is the leftmost char in a substring,
            right pointer is the rightmost. Maintain one dict of char:frequency for every
            char in the current window, and one dict for every char in s1. If the two dicts
            are equal, we know that s2 has a permutation of s1. If not, slide the right pointer
            forward, adding the char and freq to the dict, and the left pointer forward, removing
            the char and freq from the dict

            check some edge cases such as if s1 length > s2 length
        '''

        if len(s1) > len(s2):
            return False

        s1_dict = {}
        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1

        s2_substring = {}
        for i in range(len(s1)):
            s2_substring[s2[i]] = s2_substring.get(s2[i], 0) + 1

        if s1_dict == s2_substring:
            return True

    
        l = 0
        for r in range(len(s1), len(s2)):
            s2_substring[s2[r]] = s2_substring.get(s2[r], 0) + 1

            s2_substring[s2[l]] -= 1
            if s2_substring[s2[l]] == 0:
                del s2_substring[s2[l]]

            l += 1
            
            if s2_substring == s1_dict:
                return True

        return False



