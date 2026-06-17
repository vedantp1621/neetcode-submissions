class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # default dict defaults to input list if no anagram groupings found

        for word in strs: # loop through each word
            count = [0] * 26 # array of 26 values, to keep place for each possible lowercase char, refreshes for each word instance
            for letter in word: # loop through each letter
                count[ord(letter)-ord('a')] += 1 # for each letter, add to the array, giving the corresponding indexes the the number of times that letter exists in string
            anagrams[tuple(count)].append(word) # convert the array into a tuple (python cant handle arrays as keys) and pass the list of integers as the key and the word as the value. 
                                                # all future additions to this specific combination of letters will be added to the sublist
        
        return list(anagrams.values()) # return the values (aka words) from the dict



