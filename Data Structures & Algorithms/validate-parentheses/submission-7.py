class Solution:
    def isValid(self, s: str) -> bool:
        stack_1 = [] # running stack
        close_To_Open = { ")" : "(", "]" : "[", "}" : "{" } # easy pairing lookups 
        if len(s) % 2 != 0: # if there is an odd number of chars 
            return False

        for character in s: # for each cahr
            

            
            if character in close_To_Open: # checking if this char is a closing char
                if stack_1 and stack_1[-1] == close_To_Open[character]: 
                    # if the stack exists and teh top element in it 
                    stack_1.pop()
                else:
                    return False

            else: # appending the opening chars
                stack_1.append(character)
            
        return True if not stack_1 else False



            