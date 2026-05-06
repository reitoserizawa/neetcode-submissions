class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, max_area = 0, len(heights)-1, 0

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            cur_area = height * width
            max_area = max(max_area, cur_area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_area