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
        l = self.d[key]
        left = 0
        right = len(l) - 1
        ans = ""

        while left <= right:
            mid = (left + right) // 2
            if l[mid][1] == timestamp:
                return l[mid][0]
            
            if l[mid][1] <= timestamp:
                ans = l[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return ans