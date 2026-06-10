class TimeMap:

    def __init__(self):
        # {key: [(time, val)...]}
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hashMap:
            return ""
        
        l, r = 0, len(self.hashMap[key])-1
        vals = self.hashMap[key]
        val = ""
        while l <= r:
            m = (l+r) // 2
            if vals[m][1] <= timestamp:
                val = vals[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return val
