class Solution:
    def reorganizeString(self, s: str) -> str:
        # use counter and process from the most recurring character
        counter = Counter(s)

        hp = []
        for ch, freq in counter.items():
            heapq.heappush(hp, (-freq, ch))

        res = ''
        prev = None
        while hp:
            freq, ch = heapq.heappop(hp)
            
            res += ch
            freq += 1
            
            if prev:
                heapq.heappush(hp, prev)

            if freq == 0:
                prev = None
            else:
                prev = (freq, ch)
        
        if prev:
            return ""
        
        return res
