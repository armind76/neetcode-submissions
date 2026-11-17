'''
bro i struggled with this bitch
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sset = dict()
        
        for c in s1:
            sset[c] = 1 + sset.get(c,0)
        need = len(sset)
        for i in range(len(s2)):
            check = {}
            cur = 0
            for j in range(i,len(s2)):
                
                check[s2[j]] = 1 + check.get(s2[j],0) 
                if check[s2[j]] > sset.get(s2[j],0):
                    break
                if check[s2[j]] == sset.get(s2[j],0):
                    cur += 1
                if cur == need:
                    return True

        return False




        