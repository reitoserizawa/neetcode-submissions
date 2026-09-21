class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                diff = abs(x1-x2) + abs(y1-y2)
                adj[i].append((diff, j))
                adj[j].append((diff, i))

        # cost, cur
        hp = [(0, 0)]
        visited = set()
        res = 0

        while hp:
            cost, cur = heapq.heappop(hp)
            if cur in visited:
                continue

            visited.add(cur)
            res += cost

            for diff, nxt in adj[cur]:
                heapq.heappush(hp, (diff, nxt))
        
        return res