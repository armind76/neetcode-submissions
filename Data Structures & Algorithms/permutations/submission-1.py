class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []
        def backtrack(perm,nums,pick):
            if len(perm) == len(nums):
                nonlocal res
                copy_perm = perm.copy()
                res.append(copy_perm)
                return
            for i in range(len(nums)):
                if not pick[i]:
                    pick[i] = True
                    perm.append(nums[i])
                    backtrack(perm,nums,pick)
                    pick[i] = False
                    perm.pop()
        backtrack([],nums,[False]*len(nums))
        return res

            