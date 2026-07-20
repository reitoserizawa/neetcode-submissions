class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        node_cnt = {}
        leaves = deque()

        for src, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(src)
            node_cnt[src] = len(neighbors)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for src in adj[node]:
                    node_cnt[src] -= 1
                    if node_cnt[src] == 1:
                        leaves.append(src)