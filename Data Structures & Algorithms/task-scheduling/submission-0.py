class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        hp = [-freq for freq in counter.values()]
        heapq.heapify(hp)
        
        # next start time, freq
        cooldown = deque() 
        time = 0
        while hp or cooldown:
            time += 1

            if hp:
                v = 1 + heapq.heappop(hp)
                if v != 0:
                    cooldown.append((time+n, v))
            if cooldown and cooldown[0][0] == time:
                _, v = cooldown.popleft()
                heapq.heappush(hp, (v))
        return time