'''
for c in s: 
    if we seen it we skip, # TODO think about data set
    else:
        left = 0
        right = 0
        cr (current replacements) = 0
        while r < len:
            cur =  (right - left + 1)
            if (s[right] == c)


'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            l = count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                currLen = (r - l + 1)
                if currLen - count > k:
                    while currLen - count > k and l < r:
                        if s[l] == c:
                            count -= 1
                        l += 1
                        currLen = (r - l + 1)
                res = max(res,currLen)
        return res

                    