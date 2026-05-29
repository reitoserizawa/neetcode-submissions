class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                val1, val2 = stack[-1], stack[-2]
                num = int(val1)+int(val2)
                stack.append(num)
            elif op == 'D':
                val = stack[-1]
                num = int(val)*2
                stack.append(num)
            elif op ==  'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)