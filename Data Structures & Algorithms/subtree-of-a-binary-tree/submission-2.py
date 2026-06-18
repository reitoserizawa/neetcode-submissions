# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)
        
        def dfs(node1, node2):
            if not node2:
                return True
            
            if not node1:
                return False
            
            if node1.val == node2.val:
                check = isSameTree(node1, node2)
                if check: return True
            
            if node1.left:
                left = dfs(node1.left, node2)
                if left: return True
            if node1.right:
                right = dfs(node1.right, node2)
                if right: return True

            return False
        
        return dfs(root, subRoot)

