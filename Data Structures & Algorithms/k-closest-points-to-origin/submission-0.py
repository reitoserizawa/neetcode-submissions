class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []

        for i in range(len(points)):
            x, y = points[i]
            dis = math.sqrt(x**2 + y**2)
            heapq.heappush(hp, (-dis, i))
            while len(hp) > k:
                heapq.heappop(hp)
        
        res = []
        for dis, i in hp:
            res.append(points[i])
        
        return res
