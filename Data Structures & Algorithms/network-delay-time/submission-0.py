class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        
        for src, des, time in times:
            adj[src].append((des, time))
        
        visited = set()
        # start, cur_time
        hp = [(0, k)]
        
        while hp:
            time, cur = heapq.heappop(hp)
            if cur in visited:
                continue
            
            visited.add(cur)

            if len(visited) == n:
                return time
            
            for to, cost in adj[cur]:
                heapq.heappush(hp, (cost+time, to))
        
        return -1
                