'''
we want to go word by work
set it into a map
then we use that map as a key and insert the word into an array corresponding to that key
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for s in strs: 
            count = [0] * 26
            for char in s:
                count [ord(char) - ord('a')] += 1
            if tuple(count) not in res:
                res[tuple(count)] = []    
            res[tuple(count)].append(s)
        return list(res.values())
        