class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        if not queries:
            return []
        
        if not intervals:
            return [-1 for _ in range(len(queries))]

        intervals.sort(key=lambda x: x[0])
        sorted_query = sorted(queries)
        query_map = {}
        i = 0
        hq = []
        
        for q in sorted_query:
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(hq, (end-start+1, end))
                i += 1
            
            while hq and hq[0][1] < q:
                heapq.heappop(hq)
                    
            query_map[q] = hq[0][0] if hq else -1
        
        return [query_map[q] for q in queries]
