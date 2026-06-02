class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # str, open cnt, close cnt
        stack = [('', 0, 0)]
        res = []

        while stack:
            p, op, cl = stack.pop()

            if len(p) == n * 2:
                res.append(p)
                continue
            if op < n:
                stack.append([p + '(', op+1, cl])
            if cl < op:
                stack.append([p + ')', op, cl+1])
        
        return res