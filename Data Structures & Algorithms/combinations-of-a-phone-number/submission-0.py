class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keypad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        def dfs(cur,i):
            if i >= len(digits):
                return cur
            res = []
            for a in cur:
                for b in keypad[digits[i]]:
                    print(a,b)
                    res.append(a+b)
            cur = res
            return dfs(cur,i+1)
        
        tmp = keypad[digits[0]]
        return dfs(tmp,1)