class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        heapq.heapify_max(stones)
        while True:
            print(stones)
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if y == 0:
                heapq.heappush_max(stones,x)
                heapq.heappush_max(stones,y)
                break
            if x >= y:
                x = x - y
                y = 0
            else:
                y = y-x
                x = 0
            heapq.heappush_max(stones,x)
            heapq.heappush_max(stones,y)
        
        return stones[0]