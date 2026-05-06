class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [0] * n
        res = 0

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]
        
        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return 0
            
            if ranks[p1] < ranks[p2]:
                parents[p1] = p2
                ranks[p2] += ranks[p1]
            else:
                parents[p2] = p1
                ranks[p1] += ranks[p2]
            return 1

        res = n
        for a, b in edges:
            if union(a, b):
                res -= 1
        return res