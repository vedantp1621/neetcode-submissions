class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        if len(s) % 2 != 0:
            return False

        for char in s:
            
            if char in closeToOpen: #checking if closing is valid 
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False

            else: # appending the opening chars
                stack.append(char)
            
        return True if not stack else False



            