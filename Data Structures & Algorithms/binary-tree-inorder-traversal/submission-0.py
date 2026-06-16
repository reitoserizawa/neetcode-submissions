# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            
            left = dfs(node.left)
            if left:
                res.append(left.val)
            
            res.append(node.val)

            right = dfs(node.right)
            if right:
                res.append(right.val)
        
        dfs(root)
        return res