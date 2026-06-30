"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, size):
            allSame = True

            for i in range(size):
                for j in range(size):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
                        break
            
            if allSame:
                return Node(
                grid[r][c],
                True
            )

            half = size // 2
            
            topLeft = dfs(r, c, half)
            topRight = dfs(r, c+half, half)
            bottomLeft = dfs(r+half, c, half)
            bottomRight = dfs(r+half, c+half, half)

            return Node(
                grid[r][c],
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )

        return dfs(0, 0, len(grid))