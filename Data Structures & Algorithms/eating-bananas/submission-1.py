import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            count = 0
            for p in piles:
                count += math.ceil(p/k)
                if count > h:
                    return False
            
            return count <= h

        k = 1
        max_k = max(piles)

        while k < max_k:
            mid = (k+max_k)//2
            if k_works(mid):
                max_k = mid
            else:
                k = mid+1
        
        return k