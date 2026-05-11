class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]
        remainder = 0
        res = [0] * (len(num1) + len(num2)) 

        for i, n2 in enumerate(num2):
            for j, n1 in enumerate(num1):
                digit = int(n1) * int(n2)
                total = digit + res[i + j]
                res[i + j] = total % 10
                res[i + j + 1] += total // 10
        
        while res and res[-1] == 0:
            res.pop()

        return ''.join(map(str, res[::-1]))


