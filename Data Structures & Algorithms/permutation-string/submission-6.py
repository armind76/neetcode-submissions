'''
we want two different maps for this example

one is for all the characters in s1
and the other is for each iteration of a loop


need = len (s1)
first step 
 map <- all chars of s1

for i in range s2:
    check = {}, current = 0
    for j in range i,s2:
        check[s[j]]++
        if check s[j] > map[s[j]]:
            break
        else:
            current ++
        
        if current == need:
            return True
return False
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        mp = {}
        for c in s1:
            mp[c] = 1 + mp.get(c,0)
        need = len(s1)
        for i in range(len(s2)):
            check = {}
            curr = 0
            for j in range(i,len(s2)):
                check[s2[j]] = 1 + check.get(s2[j] , 0)
                if check[s2[j]] > mp.get(s2[j],0):
                    break;
                else: 
                    curr += 1
                if curr == need:
                    return True
        return False
        



        