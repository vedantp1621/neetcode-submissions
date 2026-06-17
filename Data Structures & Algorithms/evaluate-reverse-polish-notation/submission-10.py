class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in operators:  
                stack.append(tokens[i])
            else:
                var1 = stack.pop()
                var2 = float(stack.pop())
                string = f"{var2}{tokens[i]}{var1}"

                stack.append(int((eval(string))))
                
            print(stack)    

        return int(stack[0]);
