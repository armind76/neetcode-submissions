class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        prod = 1
        for num in nums:
            if num == 0:
                zeroCount += 1
                if zeroCount > 1:
                    return [0] * len(nums)
            else: 
                prod *= num
        if zeroCount == 0:
            return list(int(prod/x) for x in nums)     
        res = []            
        for num in nums:
            if num == 0:
                res.append(prod)
            else:
                res.append(0)
        return res


        