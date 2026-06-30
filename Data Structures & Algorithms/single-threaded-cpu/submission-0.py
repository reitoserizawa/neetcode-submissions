class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(start, p, i) for i, (start, p) in enumerate(tasks)])
        hp = []

        res = []
        time = 0
        i = 0

        while i < len(tasks) or hp:
            if not hp:
                time = max(tasks[i][0], time)

            while i < len(tasks) and time >= tasks[i][0]:
                s, p, index = tasks[i]
                heapq.heappush(hp, (p, index))
                i += 1
            
            p, index = heapq.heappop(hp)
            time += p
            res.append(index)

        return res
