class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = [i for i in range(n)]
        heights = [1] * (n)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            if heights[p1] > heights[p2]:
                parent[p2] = p1
                heights[p1] += heights[p2]
            else:
                parent[p1] = p2
                heights[p2] += heights[p1]
            return True
        
        for x, y in edges:
            if not union(x, y):
                return False
        return True