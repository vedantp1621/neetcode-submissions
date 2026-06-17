class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)


        for character in s:
            s_dict[character] += 1

        for character in t:
            t_dict[character] += 1

        return t_dict == s_dict



        