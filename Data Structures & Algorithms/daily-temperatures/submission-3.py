class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                tt, ii = stack.pop()
                res[ii] = i - ii
            stack.append((t, i))
        
        return res