class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = [0] * len(height)
        r_wall = [0] * len(height)
        max_l_wall = max_r_wall = 0

        for i in range(len(height)):
            l_wall[i] = max_l_wall
            r_wall[-i-1] = max_r_wall
            max_l_wall = max(height[i], max_l_wall)
            max_r_wall = max(height[-i-1], max_r_wall)
        
        res = 0
        for j in range(len(height)):
            wall = min(l_wall[j], r_wall[j])
            pot = max(0, wall-height[j])
            res += pot
        
        return res



