class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(nums,subset,i):
            if i == len(nums):
                res.append(subset[::])
                return
            subset.append(nums[i])
            backtrack(nums,subset,i+1)
            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(nums,subset,i+1)
                
        backtrack(nums,[], 0)
        return res

        