class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(cur, op, cl):
            if op > n or cl > n:
                return

            if op == n and cl == n:
                print(cur)
                res.append(''.join(cur.copy()))
                return
            
            cur.append('(')
            backtrack(cur, op+1, cl)
            cur.pop()

            if op > cl:
                cur.append(')')
                backtrack(cur, op, cl+1)
                cur.pop()
            
            # if 
            # cur.append('(')
            # backtrack(cur, op+1, cl)

            
                
        backtrack([], 0, 0)
        return res