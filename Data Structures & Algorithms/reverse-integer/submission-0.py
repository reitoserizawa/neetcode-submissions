class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        while x:
            digit = x % 10
            x //= 10

            if res > (MAX - digit) // 10:
                return 0

            res = res * 10 + digit
        
        res *= sign
        return res if MIN <= res <= MAX else 0