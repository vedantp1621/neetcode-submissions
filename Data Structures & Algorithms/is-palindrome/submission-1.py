class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # preprocessing: make life easier by keeping all 
                      # ascii values in the lower
        left, right = 0, len(s)-1 # init the left and right to the edges
        while left < right: # keeps going until left and right surpass each other
            if not s[left].isalnum(): # checks non alphanumerics, and ignores
                                      # note: we must continue to make sure
                                      # the left < right condition is still met
                                      # and the while can keep looping
                left += 1 # ignore
                continue # revisit top of loop
            if not s[right].isalnum(): # checks non alphanumerics, and ignores
                                      # note: we must continue to make sure
                                      # the left < right condition is still met
                                      # and the while can keep looping
                right -= 1 # ignore 
                continue # revisit top of loop
            if s[left] != s[right]: # not valid palindrome. after ensuring
                                    # that the two chars were comparing are 
                                    # alphanumeric, they must be equal for it
                                    # to continue checking
                return False
            else: # so far so good, the left and right chars are equal and we
                  # can continue checking
                left += 1
                right -= 1
        
        return True # if we didnt return false by now, we can assume that it
                    # is a valid palindrome

