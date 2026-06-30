class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        events = sorted(list(zip(capital, profits)))
        
        # len(hp) <= k
        # hp = [cur_total_cap, cap_needed]
        hp = []
        i = 0

        for _ in range(k):
            while i < len(events) and events[i][0] <= w:
                heapq.heappush(hp,  -1 * (events[i][1]))
                i += 1
            
            if not hp:
                break
            
            val = heapq.heappop(hp)
            w += -val
                
        return w
                    

