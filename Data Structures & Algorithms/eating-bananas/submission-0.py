'''
brute force: 
    take n in range upper bound of h/len:
        sum += upper bound(element/n)
        if sum < h:
            n ++
        else:
            return n
but we can do better with binary search 
with binary seach the issue is the upper bound and lower bound
lower bound 1 
upper bound is len(list)* math.ceil(max/h) #this step is o(n)
res = 0
while lower <= upper :
    k = lower + upper // 2
    sum = 0
    for p in piles: 
        sum += math.ceil(float(p/k))
    if sum < h:
        res = h
        lower = h + 1
    else: 
        upper = h - 1

'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = 0
        while l <= r:
            k = (l + r) //2
            totalTime =0
            for p in piles:
                totalTime += math.ceil(float(p/k))
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res


    