class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        for char in s:
            s_dict[char] = s_dict[char] + 1
        for char in t:
            t_dict[char] = t_dict[char] + 1

        print(s_dict)
        print(t_dict)

        return s_dict == t_dict

    

            
        