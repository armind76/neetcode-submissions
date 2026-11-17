class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        mp = {}
        mp[s[0]] = 1
        b = 0
        f = 1
        res = 0
        while f < len(s):
            if mp.get(s[f],0) == 0 or f == b:
                mp[s[f]] = 1
                f += 1
                res = max(res,f-b)

            else:
                mp[s[b]] -= 1
                b += 1

        return res



        '''
        idk if this will work but lets just full send it and figure out

        so the idea is that we make a mpa
        and we have two pointers
        we start at index 0 and 1
        first step is to add index 0 and 1 to the map
        EDGE CASE: if there is 0 or 1
        so the first pointer starts at 0 and the second pointer starts at 1
        if the letter at 1 is a new one 
        we wanna add that to the map
        if its already seen we want to move the one thats behind and remove said       
        letters
        idk if this will work but lets 
        '''
        