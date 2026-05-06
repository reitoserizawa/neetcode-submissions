class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            n = len(s)
            res += f'{n}#{s}'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            word = s[j+1:j+l+1]
            res.append(word)
            i = j+l+1
        return res
        