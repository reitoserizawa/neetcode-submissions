class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        
        visited = set()
        def dfs(cur):
            if cur in visited:
                return
            
            visited.add(cur)
            for nei in adj[cur]:
                if nei in visited:
                    continue
                dfs(nei)
        
        res = 0
        for i in range(n):
            if not i in visited:
                dfs(i)
                res += 1
        return res