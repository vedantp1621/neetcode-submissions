class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)


        for i in range(len(strs)):
            key = [0] * 26
            for char in strs[i]:
                key[ord(char) - ord('a')] += 1
            output[tuple(key)].append(strs[i])

        return list(output.values())

            

       
             

        