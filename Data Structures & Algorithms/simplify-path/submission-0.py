class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        
        for p in path:
            if p == '.' or p == '':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(p)
        
        return '/'+ '/'.join(stack)