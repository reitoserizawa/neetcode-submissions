class TimeMap:

    def __init__(self):
        self.d = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((value, timestamp))
        else:
            self.d[key] = [(value, timestamp)]
        
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.d:
            return ""

        items = self.d[key]
        l, r = 0, len(items)-1
        res = ""
        while l <= r:
            mid = (l+r)//2
            if items[mid][1] == timestamp:
                return items[mid][0]
            if timestamp > items[mid][1]:
                res = items[mid][0]
                l = mid+1
            else:
                r = mid-1
        
        return res