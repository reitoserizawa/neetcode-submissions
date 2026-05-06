class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        visited = set()
        def dfs(n):
            visited.add(n)

            for nei in adj[n]:
                if nei in visited:
                    continue
                visited.add(nei)
                dfs(nei)

        c = 0        
        for i in range(n):
            if i not in visited:
                dfs(i)
                c += 1
        return c