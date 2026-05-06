class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, container = [], []

        def helper(openn, close):
            if len(container) ==  n*2:
                res.append(''.join(container))
                return
            if openn < n:
                container.append('(')
                helper(openn+1, close)
                container.pop()
            if openn > close:
                container.append(')')
                helper(openn, close+1)
                container.pop()
        
        helper(0, 0)
        return res
