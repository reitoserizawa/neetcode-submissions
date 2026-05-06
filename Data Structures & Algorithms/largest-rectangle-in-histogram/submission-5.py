class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_h = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                hh, ii = stack.pop()
                max_h = max(max_h, hh*(i - ii))
                start = ii
            stack.append((h, start))
        
        for h, i in stack:
            w = len(heights)-i
            max_h = max(max_h, h*w)
        
        return max_h