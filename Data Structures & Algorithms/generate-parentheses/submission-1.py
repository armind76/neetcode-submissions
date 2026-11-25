class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        use back tracking 
        base case is index == n
         add to res
         return
        recursive step:
            add ( to the string
            recursive call
            add)
            recursive call
        
        '''
        res = []
        def backtrack(closeCnt,cur,openCnt):
            #base:
            if closeCnt == n and openCnt == n:
                res.append(cur)
                return
            if openCnt < n:
                backtrack(closeCnt,cur + "(",openCnt+1)
            if closeCnt < openCnt:
                backtrack(closeCnt+ 1,cur + ")",openCnt)
        backtrack(0,"",0)
        return res