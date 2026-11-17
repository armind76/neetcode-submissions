'''
we want to implement binary search


0 0 0 
0 0 0 
0 0 0 

len = 8
int (8 / 2) = 4
4 / 3 = 1
4 % 3 = 1
~~~~~~~~~~~~~~~~
0 0 0 0 
0 0 0 0
0 0 0 0
len = 4 * 3 - 1 = 11 
11 / 2 = 5
5 / 3 = 1
5 % 4 = 1

algorithm:
#if list = []:
#    reutrn False
row = len(list)
col = len(list[0])
left = 0
right = row * col - 1

while left < right:
    mid = (left + right)/2
    cur = list[int(mid/row)][mid % col]
    if target == cur:
        return true
    elif target < cur:
        right = mid
    elif:
        left = mid + 1



'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1

        while left <= right:
            mid = left + (right - left)//2
            cur = matrix[mid//col][mid % col]
            if target == cur:
                return True
            elif target < cur:
                right = mid - 1
            else:
                left = mid + 1
        return False
        