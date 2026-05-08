class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = 0

        while n not in seen:
            seen.add(n)

            strNum = str(n)
            cur = 0
            for strN in strNum:
                cur += int(strN) * int(strN)
            
            if cur == 1:
                return True
                
            n = cur
        
        return False