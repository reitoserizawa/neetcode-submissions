class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^n = (x^(n//2))^2 if n is even else x * (x^(n//2))^2

        def calculatePow(a, b):
            if a == 0:
                return 0
                
            if b == 0:
                return 1
            
            half = calculatePow(a, b // 2)

            if b % 2 == 0:
                return half * half
            return half * half * a
        
        if n < 0:
            x = 1 / x
            n = -n

        return calculatePow(x, n)