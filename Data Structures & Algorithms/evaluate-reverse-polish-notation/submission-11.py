class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"} # map to detect the operators in O(1)
        stack = [] # stores the numbers to aggragate when we find the operator

        for i in range(len(tokens)): # loop through each token
            if tokens[i] not in operators: # if the token is not an operator, populate the stack
                stack.append(tokens[i])
            else: # otherwise, we will do an operation with two tokens, as per the RPN pattern
                var1 = stack.pop() # we will always do b operator a, to account for subtraction
                var2 = float(stack.pop()) # we want output of b opp a to be a float, so we only need
                                          # one variable to be a float
                string = f"{var2}{tokens[i]}{var1}" # create a string representing the one by one operation

                stack.append(int((eval(string)))) # use eval to calculate the string, and cast to int to 
                                                  # truncate downwards
                
        return int(stack[0]); # return the casted int of the final value in the stack, which will be a float
