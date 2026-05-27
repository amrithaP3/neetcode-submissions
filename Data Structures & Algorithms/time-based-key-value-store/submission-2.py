class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((value, timestamp))
        else:
            self.timemap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        values = self.timemap[key]
        largest = 0
        res = ""
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            
            if values[mid][1] <= timestamp:
                if values[mid][1] > largest:
                    largest = values[mid][1]
                    res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res

        
