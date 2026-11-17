'''
so ok we want to keep a stack of the previous temperatures
while the current temperature is less than the top element of the
stack we will just add the current temp in the array
'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT,stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append([t,i])
        return res
            
            
        
        
