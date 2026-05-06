class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # max_area = 0
        # stack = []

        # for i, h in enumerate(heights):
        #     start = i
        #     while stack and stack[-1][1] > h:
        #         ind, height = stack.pop()
        #         max_area = max(max_area, height * (i-ind))
        #         start = ind
        #     stack.append((start, h))
        
        # for i, h in stack:
        #     max_area = max(max_area, h * (len(heights)-i))
        
        # return max_area
        max_area = 0
        stack = []  # Stores indices of heights

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            
            stack.append(i)

        # Process remaining elements in the stack
        while stack:
            h = heights[stack.pop()]
            w = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, h * w)
        
        return max_area