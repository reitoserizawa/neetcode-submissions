class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        OPERATORS = ['+', '-', '*', '/']

        for t in tokens:
            if t in OPERATORS:
                if t == '+':
                    val1, val2 = stack.pop(), stack.pop()
                    stack.append(val2 + val1)    
                elif t == '-':
                    val1, val2 = stack.pop(), stack.pop()
                    stack.append(val2 - val1)    
                elif t == '*':
                    val1, val2 = stack.pop(), stack.pop()
                    stack.append(val2 * val1)    
                elif t == '/':
                    val1, val2 = stack.pop(), stack.pop()
                    stack.append(int(val2 / val1))    
            else:
                stack.append(int(t))
        
        return stack[-1]