class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(cur):
            if cur in visited:
                return
            visited.add(cur)
            for nei in adj[cur]:
                if nei not in visited:
                    dfs(nei)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res

            
                