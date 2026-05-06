class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack =[]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, ind = stack.pop()
                maxArea = max(maxArea, height * (i - ind))
                start = ind
            stack.append((h, start))

        for h, i in stack:
            w = len(heights) - i
            maxArea = max(maxArea, h * w)
        
        return maxArea