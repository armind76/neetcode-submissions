'''
map = {key : [(time , value), (time, value)]}

set
map[key].push((time, value))
get:
letf , right
mid the midle of  left and right

while left < right
if middle == value
return value
value < target :
right = middle - 1
else 
left = middle + 1 

'''

class TimeMap:
    mp ={}
    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append((timestamp,value))
 
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        l,r = 0, len(self.mp[key]) - 1
        res = ""
        while l <= r:
            m = (l+r)//2
            time,value = self.mp[key][m]
            if time <= timestamp:
                l = m + 1
                res = value
            else:
                r = m - 1
        return res

        
