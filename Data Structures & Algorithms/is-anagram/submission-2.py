class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict = dict()
        tdict = dict()
        i = 0
        while i < len(s):
            sdict[s[i]] = 1 + sdict.get(s[i], 0)
            tdict[t[i]] = 1 + tdict.get(t[i], 0)
            i += 1
        return sdict == tdict
        