class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        for this, i believe we use a default dict of type set. 
        for each str, we build the set and then append that set to the default dict, finally returnign that dict
        '''
        
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values()) 
    
             

        