# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ''
        q = deque([root])

        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if n:
                    res += str(n.val)+'#'
                    q.append(n.left)
                    q.append(n.right)
                else:
                    res += 'N#'
        
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split('#')
        
        if arr[0] == 'N':
            return None

        root = TreeNode(int(arr[0]))
        q = deque([root])
        i = 1

        while q and i < len(arr):
            n = q.popleft()

            if arr[i] != 'N':
                left = TreeNode(int(arr[i]))
                n.left = left
                q.append(left)
            i += 1
            
            if i < len(arr) and arr[i] != 'N':
                right = TreeNode(int(arr[i]))
                n.right = right
                q.append(right)
            i += 1
        
        return root

            



