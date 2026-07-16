class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n+1)]
        rank = [0] * (n+1)

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
    
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return True
            
            if rank[root_x] < rank[root_y]:
                parents[root_y] = root_x
                rank[root_x] += rank[root_y]
            else:
                parents[root_x] = root_y
                rank[root_y] += rank[root_x]
            
            return False
        

        for a, b in edges:
            if union(a, b):
                return [a, b]

