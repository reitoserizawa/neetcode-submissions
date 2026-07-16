class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        parents = [i for i in range(n)]
        rank = [1] * n
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if rank[root_x] < rank[root_y]:
                parents[root_x] = root_y
                rank[root_y] += rank[root_x]
            else:
                parents[root_y] = root_x
                rank[root_x] += rank[root_y]
            
            return True
        
        for a, b in edges:
            if not union(a, b):
                return False
            
        return True