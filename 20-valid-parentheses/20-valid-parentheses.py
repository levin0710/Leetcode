class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for par in s:
            if par == '(' or par == '[' or par =='{':
                stack.append(par)
            else:
                if len(stack) == 0:
                    return False
                openBracket = stack.pop()
                if par == ')' and openBracket != '(':
                    return False
                elif par == ']' and openBracket != '[':
                    return False
                elif par == '}' and openBracket != '{':
                    return False
        return len(stack) == 0