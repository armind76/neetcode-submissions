class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse = True)

        stack = []
        stack.append((target - pair[0][0])/pair[0][1])
        for i in range(1,len(pair)):
            time = (target - pair[i][0])/pair[i][1]
            if time > stack[-1]:
                stack.append(time)

        return len(stack)
