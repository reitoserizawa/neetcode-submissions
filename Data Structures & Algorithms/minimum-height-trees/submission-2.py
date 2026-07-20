class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, visited):                
            if node in visited:
                return 0
            
            visited.add(node)
            height = 0

            for child in adj[node]:
                height = max(height, dfs(child, visited))
            
            return height + 1

        heights = []
        for i in range(n):
            h = dfs(i, set())
            heights.append(h)
        
        mhs = min(heights)
        print(heights)
        return [i for i, n in enumerate(heights) if n == mhs]

        