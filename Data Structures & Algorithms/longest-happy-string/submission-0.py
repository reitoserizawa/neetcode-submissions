class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hp = []

        if a:
            heapq.heappush(hp, (-a, 'a'))
        if b:
            heapq.heappush(hp, (-b, 'b'))
        if c:
            heapq.heappush(hp, (-c, 'c'))

        res = []
        while hp:
            freq, ch = heapq.heappop(hp)

            if len(res) >= 2 and res[-1] == res[-2] == ch:
                if not hp:
                    break

                freq2, ch2 = heapq.heappop(hp)
                freq2 += 1
                res.append(ch2)

                if freq2:
                    heapq.heappush(hp, (freq2, ch2))
                
                heapq.heappush(hp, (freq, ch))
            else:
                freq += 1
                res.append(ch)
                if freq:
                    heapq.heappush(hp, (freq, ch))
        return ''.join(res)