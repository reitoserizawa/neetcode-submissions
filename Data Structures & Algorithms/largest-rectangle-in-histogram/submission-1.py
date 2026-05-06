class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                max_area = max(max_area, height * (i-ind))
                start = ind
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights)-i))
        
        return max_area
        
