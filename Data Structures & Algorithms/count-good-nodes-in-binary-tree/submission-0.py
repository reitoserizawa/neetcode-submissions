# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        
        def dfs(node, cur):
            if not node:
                return
            
            if node.val >= cur:
                self.cnt += 1
            
            dfs(node.left, max(cur, node.val))
            dfs(node.right, max(cur, node.val))

            return node
        
        dfs(root, root.val)
        
        return self.cnt
            