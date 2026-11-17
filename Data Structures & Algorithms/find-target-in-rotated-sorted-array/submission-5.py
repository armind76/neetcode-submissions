'''
regular binary search:
    left        middle         right
    left middle right xxxxxxxxxxxxxx
we check if middle is target
if yes
we return middle
elif target < middle
right = midle - 1
else 
 left = middle + 1
special cases for this problem

4,5,6,1,2
if target is  4
target < middle :
    target >= left:
        right = middle - 1
    target < left:
        left = middle + 1

next case    
4,5,0,1,2
if target is  4
target > middle
    target < right:
        left = mid + 1
    target > right:
        right = mid - 1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target  == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1  



