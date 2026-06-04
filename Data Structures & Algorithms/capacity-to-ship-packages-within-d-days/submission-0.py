class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days == len(weights):
            return max(weights)

        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l+r) // 2
            cnt = 0
            cnt_days = 1
            for w in weights:
                cnt += w
                if cnt > mid:
                   cnt_days += 1
                   cnt = w
            if cnt_days > days:
                l = mid + 1
            else:
                r = mid
        
        return l