class Solution:
    
    # def encode(self, strs: List[str]) -> str:
    #     encoded = '' # initially empty string
    #     for string in strs: # loop through each string in original list 
    #         encoded += str(len(string)) # get length of current string and make the first letter 
    #                                     # in section the length of the string
    #         encoded += string # add string as body of section
    #         encoded += '%' # add arbitrary % character to signify end of string
    #     return encoded # return
    def encode(self, strs: List[str]) -> str:
        res = "" # initially empty string
        for s in strs: # loop through each string in array
            res += str(len(s)) + "#" + s # add length of string, then placeholder then word
        return res # return this encoded string: ex -> 4#neet4#code4#love3#you

    def decode(self, s: str) -> List[str]:
        res = [] # init empty array
        i = 0 # left ticker
        
        while i < len(s): # loop through each char in encoded string: 4#neet4#code4#love3#you
            j = i # right ticker, initialize at left
            while s[j] != '#': # stop at # to get the length of string
                j += 1 # inc right window
            length = int(s[i:j]) # cut this window out to get just the int for the length
            
            i = j + 1 # set left as one more than right window (start of word)
            j = i + length # set right as the end of the word (left+length of word)
            res.append(s[i:j]) # add this entire window
            i = j # shift entire window by setting left to right
        return res # return all strings once done

        
