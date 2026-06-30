class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort 'from', 'to', 'cap'
        trips = sorted(trips, key=lambda x: x[1]) 
        hp = []
        cur = 0

        for num, f, t in trips:
            while hp and hp[0][0] <= f:
                end_time, cap = heapq.heappop(hp)
                cur -= cap
            
            heapq.heappush(hp, (t, num))
            cur += num

            if cur > capacity:
                return False
        
        return True

