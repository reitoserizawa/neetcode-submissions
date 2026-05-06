class TimeMap:

    def __init__(self):
        self.d = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((value, timestamp))
        else:
            self.d[key] = [(value, timestamp)]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        items = self.d[key]
        l, r, pos = 0, len(items)-1, -1

        while l <= r:
            mid = (l+r)//2
            if items[mid][1] <= timestamp:
                l = mid + 1
                pos = mid
            else:
                r = mid - 1
        
        return items[pos][0] if pos != -1 else ""
