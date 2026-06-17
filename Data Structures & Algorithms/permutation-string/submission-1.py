class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False # if the lenght of s1 is bigger than s2, than there is no way this can result in
                                           # True

        s1Count, s2Count = [0] * 26, [0] * 26 # initialize an array of 26 zeros. each index corresponds to a-z. This array will
                                              # track the occurance of the letters in the strings
        for i in range(len(s1)): # loop through entire window. The window will be the size of s1, so we can initialize
                                 # the entire s1 in s1Count, and the initial window in s2Count
            s1Count[ord(s1[i]) - ord('a')] += 1 # basic mapping function, youre basically
                                                # having the index be how far away the char is
                                                # from 'a'
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0 # initialize the matches tracker to 0. this var will be checking how many of the 26 total corresponding
                    # indexes are equal between both arrays
        for i in range(26): # loop through each element in the arrays and count how many between the two are equal (max is all 26)
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        left = 0 # basic sliding window algo, initialize the left pointer to 0
        for right in range(len(s1), len(s2)): # this is meant to start at the char after the initial window, and iterate by 1 until the
                                              # end
            if matches == 26: return True # if at any point we have all matches, return True, the windows are the same

            # in this algo, we are comparing the static s1 array that has all its character occurances, and the dynamic s2 array that
            # we will update based on the current sliding window

            # ADDING A CHARACTER FROM THE RIGHT
            index = ord(s2[right]) - ord('a') # decrypt the hashing function to get the index of the current char in s2
            s2Count[index] += 1 # add the occurance of this char in the corresponding index for the windows array

            if s1Count[index] == s2Count[index]: # checks if adding the right char added a match
                matches += 1 # 'they werent equal, but now they are'
            elif s1Count[index] == s2Count[index] - 1: # checks if adding the right char removed a match
                matches -= 1 # 'they were equal, but now theyre not'

            # REMOVING A CHARACTER FROM THE LEFT
            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1 # remove the corresponding occurance
            
            if s1Count[index] == s2Count[index]: # checks if removing the left char added a match
                matches += 1 # 'they werent equal, but now they are'
            elif s1Count[index] == s2Count[index] + 1: # checks if removing the left char removed a match
                matches -= 1 # 'they were equal, but now theyre not'
            left += 1

        return matches == 26 # if at the very end, we have all matches, we can return True, else return false


        