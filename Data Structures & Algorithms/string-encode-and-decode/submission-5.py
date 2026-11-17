'''
we want to add the texts together in a way where we can decode later
we can always encode with a number corresponding to the char length
but we also need to know when the number ends so we can assign a special character
to that as well so we allways know that out words start with
char_len#word
encode: 
    res = ""
    for s in strs:
        res += len(s)
        res += #
        res += s
    return res
decode: 
    size = len(s)
    i = 0
    for i < size:
        count = ""
        while s[i] != #:
            count += c
            i++
        j= 0
        wordSize = int(count)
        while j < wordSize + i:
            word += s[j]
        i = i + j
        i++


'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        size = len(s)
        i = 0
        while i < size:
            count = ""
            while s[i] != '#':
                count += s[i]
                i += 1
            j= 0
            wordSize = int(count)
            word = ""
            while j < wordSize:
                word += s[i+j+1]
                j += 1
            res.append(word)
            i = i + j
            i +=1
        return res