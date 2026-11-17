'''
brute force algo:
start at index 0
while element at i < i + 1 and i + 1 < len: 
    i ++
    if i + 1 is the end of the list we return 0 otherwise
    return i + 1

binary search: 
l = 0
r = len (list)
while l <= r:
    if l == r:
        return l
    m = l + (r-l)/2
    if list[mid] < list[r]:
        # [4,5,1,2,3]
        left = mid
    else: 
        right = mid

'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r)//2
            res = min (res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res


                