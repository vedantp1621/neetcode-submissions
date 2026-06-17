class Solution:
    def isValid(self, s: str) -> bool:
        stack_1 = []
        close_To_Open = { ")" : "(", "]" : "[", "}" : "{" }

        if len(s) % 2 != 0:
            return False

        for character in s:
            
            if character in close_To_Open: #checking if closing is valid 
                if stack_1 and stack_1[-1] == close_To_Open[character]:
                    stack_1.pop()
                else:
                    return False

            else: # appending the opening chars
                stack_1.append(character)
            
        return True if not stack_1 else False



            