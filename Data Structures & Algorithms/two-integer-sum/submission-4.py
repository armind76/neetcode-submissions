'''
we want to use a map

map = {target-num : index}

current num and see if its in the dictionary already and if not we add it to the dictionary
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = dict()
        i = 0
        size = len(nums)
        while i < size: 
            if nums[i] in check:
                return [check[nums[i]],i]
            check[target - nums[i]] = i
            i+=1
        
        