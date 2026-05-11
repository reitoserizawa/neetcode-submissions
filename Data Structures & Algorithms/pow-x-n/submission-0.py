class Solution:
    def myPow(self, x: float, n: int) -> float:
        # val = x ** n == val == n / 2 ** n / 2
        # val = x ** n == val == x ** n / 2 * x ** n / 2

        def calculatePow(a, b):
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