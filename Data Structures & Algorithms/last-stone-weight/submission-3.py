class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []

        for s in stones:
            heapq.heappush(hp, -s)
        
        while len(hp) > 1:
            x, y = heapq.heappop(hp), heapq.heappop(hp)
            x, y = x * -1, y * -1
            if x == y:
                continue
            elif x > y:
                heapq.heappush(hp, -(x-y))
            
        return -hp[0] if hp else 0
