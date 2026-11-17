'''
count = [0]*26

map = {count:[a,b,c]}
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict() 
        for s in strs: 
            count = [0]*26
            for c in s:
                count [ord(c) - ord('a')] += 1
            if tuple(count) not in res:
                res[tuple(count)] = list()
            res[tuple(count)].append(s)
        return list(res.values())

        