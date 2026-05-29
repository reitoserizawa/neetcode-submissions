class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in ['(', '[', '{']:
                stack.append(p)
            else:
                if not stack or (p == ')' and stack[-1] != '(') or (p == ']' and stack[-1] != '[') or (p == '}' and stack[-1] != '{'):
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0