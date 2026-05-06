class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = ")}]"

        for i in range(len(s)):
            cur = s[i]
            if cur in closing:
                if not stack:
                    return False
                opening = stack.pop()
                if (opening == '(' and not cur == ')') or (opening == '[' and not cur == ']') or (opening == '{' and not cur == '}'):
                    return False
            else:
                stack.append(s[i])

        return True if len(stack) == 0 else False

        