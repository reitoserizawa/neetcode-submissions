class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        parents = [i for i in range(n)]
        rank = [0] * n

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]
        
        def union(x, y):
            p1, p2 = find(x), find(y)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += p1
            return True

        for a, b in edges:
            if not union(a, b):
                return False
        return True