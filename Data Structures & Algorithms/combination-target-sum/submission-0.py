class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def validate(subNums,i,sum):
            #base case:
            nonlocal nums
            nonlocal target
            if sum > target or i >= len(nums):
                return
            if sum == target:
                res.append(subNums.copy())
                return
            #recursive
            subNums.append(nums[i])
            validate(subNums,i,sum +nums[i])
            subNums.pop()
            validate(subNums,i+1,sum)
        
        validate([],0,0)
        return res

