    # Stack: FIFO

    # '''
    # Thought process:

    # Prelims: The pattern is that the first last element must match
    #          Then, if you pop those, the next first and last elements
    #          must match

    # To identify if a character is the correct part of a pair, we will
    # use a hash map that is prefilled with the parts. The keys will be closing
    # and the values will be opening

    # First Condition: Check if the iter char is an opening or closing peice,
    # using 'in', which checks all keys
    #     True: means that iter is a closing peice (stack should have all 
    #     opening peices)
    #     False: means that iter is an opening peice, so we add to stack

    # Now we will iterate through the string

    # Second Condition: Check is the stack nonempty and is the element 
    # in the stack part of the pair with the iter element
    #     True: pop from stack
    #     False: return False

    # Once iteration is done:
    # Return false if stack is nonempty
    # Return true if stack is empty
    # '''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}       
        
        for character in s:
            if character in pairs:
                if stack and stack[-1] == pairs[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)

        if stack:
            return False
        else: 
            return True