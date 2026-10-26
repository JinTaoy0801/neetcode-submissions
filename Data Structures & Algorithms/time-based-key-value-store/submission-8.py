class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = [[value,timestamp]]
        else:
            self.mp[key].append([value,timestamp])
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp :
            return ""
        
        l = 0
        r = len(self.mp[key]) -1
        ans = ""
        while l <= r:
            mid = (l+r)//2
            timestamp_prev = self.mp[key][mid][1]
            if timestamp_prev <= timestamp:
                ans = self.mp[key][mid][0]
                l = mid +1
            else :
                r = mid - 1
        return ans
        
