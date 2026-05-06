class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, max_area = 0, len(heights)-1, 0

        while l < r:
            min_bar = min(heights[l], heights[r])
            max_area = max(max_area, min_bar * (r-l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
