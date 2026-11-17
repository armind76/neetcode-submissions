'''
s = {[()]}
i want to go over all the elements in s ^ 
if its an oppening i want to push it into our stack (a list)

and else (is closing) we want to pop,
if the popped element isnt the same as the closing we return false

and if we get to the end of the string and our stack is empty we return true

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checker = {'(':')','{':'}','[':']'}
        for c in s: 
            if c in checker:
                stack.append(c)
            else:
                if stack == []:
                    return False 
                close = stack.pop()
                if c != checker[close]:
                    return False
        return stack == []