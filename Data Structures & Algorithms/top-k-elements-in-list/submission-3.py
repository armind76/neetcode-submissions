class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        frequency = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums: 
            counter[num] = 1+ counter.get(num, 0)
        for num in counter:
            frequency[counter[num]].append(num)
        i = len(frequency) - 1
        while i >= 0: 
            if frequency[i]:
                for j in frequency[i]:
                    res.append(j)

                if len(res) == k:
                    return res
            i -= 1
