class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        PHONE = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []

        if digits == '':
            return res

        def dfs(i, cur):
            if len(cur) == len(digits):
                cur = ''.join(cur)
                res.append(cur)
                return
            
            for letter in PHONE[digits[i]]:
                cur.append(letter)
                dfs(i+1, cur)
                cur.pop()
        
        dfs(0, [])
        return res