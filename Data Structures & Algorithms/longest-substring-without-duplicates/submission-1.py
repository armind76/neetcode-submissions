'''
res = 0
set()
char in s:
set <- char
if len(set)prior == len(set)now
set curr len = 1
set = set()
else 
cur len++
res = max(res,cur len)
return res
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        mp = {}
        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res,r-l+1)
        return res

