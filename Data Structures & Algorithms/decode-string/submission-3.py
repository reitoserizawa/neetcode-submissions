class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for l in s:
            if l == ']':
                parts = []
                while stack[-1] != '[':
                    parts.append(stack.pop())
                cur = ''.join(reversed(parts))
                stack.pop()
                cnt = ''
                while stack and stack[-1].isdigit():
                    cnt += stack.pop()
                cnt = cnt[::-1]
                stack.append(cur * int(cnt))
            else:
                stack.append(l)
        
        return ''.join(stack)