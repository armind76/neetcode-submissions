class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                fterm = int(stack.pop())
                sterm = int(stack.pop())
                stack.append(fterm + sterm)
            elif t == '-':
                sterm = int(stack.pop())
                fterm = int(stack.pop())
                stack.append(fterm - sterm)
            elif t == '*':
                sterm = int(stack.pop())
                fterm = int(stack.pop())
                stack.append(fterm * sterm)
            elif t == '/':
                sterm = int(stack.pop())
                fterm = int(stack.pop())
                stack.append(fterm / sterm)
            else: 
                stack.append(t)
        return int(stack[0])