class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        due to the fact that ther eis a need for backtracking this
        problem cannot be done properly with a nested loop imo
        res = []
        back tracking
            nonlocal res
            basecase:
                sum > target or i >= len of list
                    return
                sum == target
                    add to res
                    return
            recursive:
            cur.append(candidates[i])
            backtracking(cur:list, i , sum + candidates[i])
            cur.pop()
            backtracking(cur,i+1,sum)
        '''
        res = set()
        candidates.sort()
        def validate(cur,i,sum):
            nonlocal res
            nonlocal target
            nonlocal candidates
            #base:
            if sum == target:
                res.add(tuple(cur))
                return
            if sum > target or i >= len(candidates):
                return 
            

            #recursive:
            cur.append(candidates[i])
            validate(cur,i + 1,sum + candidates[i])
            cur.pop()
            validate(cur,i + 1,sum)
        validate([],0,0)
        return [list(x) for x in res]

