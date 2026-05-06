class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, container = [], []

        def dfs(openn, close):
            if len(container) == n*2:
                res.append(''.join(container))
                return
            if openn < n:
                container.append('(')
                dfs(openn+1, close)
                container.pop()
            if openn > close:
                container.append(')')
                dfs(openn, close+1)
                container.pop()
        
        dfs(0, 0)
        return res
