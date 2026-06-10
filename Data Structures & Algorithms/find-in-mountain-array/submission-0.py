class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2

            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            else:
                r = m

        peak = l
        
        def ascending(l, r):
            res = -1
            while l <= r:
                m = (l+r) // 2
                v = mountainArr.get(m)
                if v == target:
                    return m
                elif v > target:
                    r = m - 1
                else:
                    l = m + 1
            return res
        
        def descending(l, r):
            res = -1
            while l <= r:
                m = (l+r) // 2
                v = mountainArr.get(m)
                if v == target:
                    return m
                elif v > target:
                    l = m + 1
                else:
                    r = m - 1
            return res

        resA = ascending(0, peak)
        resB = descending(peak+1, n-1)

        if resA != -1:
            return resA
        return resB