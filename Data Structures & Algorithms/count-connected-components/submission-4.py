class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        size = [1] * n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)

            if root_x == root_y:
                return 0
            
            if size[root_x] < size[root_y]:
                parents[root_x] = root_y
                size[root_y] += size[root_x]
            else:
                parents[root_y] = root_x
                size[root_x] += size[root_y]
            
            return 1
        
        res = n
        for x, y in edges:
            res -= union(x, y)
        
        return res