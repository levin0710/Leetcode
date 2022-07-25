class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = {"+": 0, "-": 0, "*": 0, "/": 0}
        
        for token in tokens:
            if token not in symbols:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                
                if token == "+":
                    stack.append(num2 + num1)
                elif token == "-":
                    stack.append(num2 - num1)
                elif token == "*":
                    stack.append(num2 * num1)
                elif token == "/":
                    stack.append(int(float(num2)/num1))
        return stack[0]