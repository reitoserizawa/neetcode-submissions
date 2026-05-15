class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        hq = []

        for key, cnt in counter.items():
            heapq.heappush(hq, (cnt, key))
            if len(hq) > k:
                heapq.heappop(hq)
        
        return [h[1] for h in hq]