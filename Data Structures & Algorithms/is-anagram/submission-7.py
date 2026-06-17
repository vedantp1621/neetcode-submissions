class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int) # use defaultdict to store occurances of letters
        t_dict = defaultdict(int) # reasoning: default value of 0 ensures no errors with addition
        
        for char in s: # iterate through s
            s_dict[char] = s_dict[char] + 1 # count occurances
        for char in t: # iterate through t
            t_dict[char] = t_dict[char] + 1 # count occurances

        return s_dict == t_dict # if the two dicts equal, valid anagrams

    

            
        