'''
for the O(n) solution of the porblem we can only go through the entire problem once
we need to use a data structure that can retrive data in O(1) 
one such data structure is a Map

num in nums:
    map[num] = map[num-1] + map[num+1] + 1
    map[num + map[num+1]] = map[num]
    map[num - map[num-1]] = map[num]
    res = max(map[num] , res)
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        mp = {}

        for num in nums:
            if num not in mp:
                mp[num] = mp.get(num-1,0) + mp.get(num+1,0) + 1
                mp[num + mp.get(num+1,0)] = mp[num]
                mp[num - mp.get(num-1,0)] = mp[num]
                res = max(res,mp[num])
        return res
        