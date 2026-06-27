class Solution: # essentially a two pointer approach

    # list of strs -> str
    def encode(self, strs: List[str]) -> str:
        # format: [length][null term][str]
        final_str = ""
        for word in strs:
            final_str += str(len(word)) + '#' + word

        return final_str


    # str -> list of strs
    def decode(self, s: str) -> List[str]:
        res = []
        word_jump = 0

        while word_jump < len(s): # go char by char
            char_iter = word_jump
            
            while s[char_iter] != '#':
                char_iter += 1

            length = int(s[word_jump:char_iter])
            word_jump = char_iter + 1
            char_iter = length + word_jump
            res.append(s[word_jump:char_iter])
            word_jump = char_iter

        return res
            


