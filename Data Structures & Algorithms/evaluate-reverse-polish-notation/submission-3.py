# class Solution:

    #  '''

    #     tokens=["2","1","+","3","*"]
    #     stdout=['*', '3', '+', '1', '2']

    #  '''

    # def evalRPN(self, tokens: List[str]) -> int:
    #     operators = {"+", "-", "*", "/"}
    #     stack = []

    #     for i in range(len(tokens)):
    #         if tokens[i] not in operators:  
    #             stack.append(tokens[i])
    #         else:
    #             var1 = stack.pop()
    #             var2 = stack.pop()
    #             string = f"{var2}{tokens[i]}{var1}"

    #             stack.append(math.floor(eval(string)))
    #             print(stack)

    #     return stack[0];




class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
            print(stack)
        return stack[0]
