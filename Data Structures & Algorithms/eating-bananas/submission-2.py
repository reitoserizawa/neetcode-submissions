class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, piles[-1]

        while l < r:
            mid = (l+r) // 2
            cnt = 0
            for p in piles:
                cnt += math.ceil(p / mid)
            if cnt <= h:
                r = mid
            else:
                l = mid+1
        
        return l