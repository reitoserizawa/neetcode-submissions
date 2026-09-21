class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # After i iterations, dist[x] = cheapest price to reach x using at most i flights.
        dp = [float('inf') for _ in range(n)]
        dp[src] = 0
        
        for _ in range(k+1):
            temp = dp.copy()
            for frm, to, price in flights:
                if temp[frm] != float('inf'):
                    temp[to] = min(temp[to], dp[frm]+price)
            dp = temp
        
        return dp[dst] if dp[dst] != float('inf') else -1