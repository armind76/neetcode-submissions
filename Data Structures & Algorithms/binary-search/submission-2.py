'''
binary search:
we go to the index that is right in the middle of the list 
then we check
l = 0
r = len()/2
mid = (l + r)/2
if == target:
    return index
if > target:
    left = mid + 1
    calc mid
if < target: 
    right = mid - 1

[1,2,3,4,5] (target 4)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            m = int((l + r)/2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m + 1
        return -1
