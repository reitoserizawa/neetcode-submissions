class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            total = (n >> i) & 1
            res |= total << 31-i
        return res
