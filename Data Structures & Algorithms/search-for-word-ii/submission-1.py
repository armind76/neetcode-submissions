class Node:
    def __init__(self):
        self.children = {}
        self.wordEnd = False
        self.word = None
def nodify(words):
    root = Node()
    for word in words:
        cur = root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.wordEnd = True
        cur.word = word
    return root

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = nodify(words)
        if not board:
            return []
        imax = len(board)
        jmax = len(board[0])
        res = set()
        def verify(node,i,j,visited):
            if i < 0 or j >= jmax or j < 0 or i >= imax or ((i,j) in visited):
                return
            if board[i][j] in node.children:
                if node.children[board[i][j]].wordEnd:
                    res.add(node.children[board[i][j]].word)
                if (i,j) not in visited:
                    visited.add((i,j))

                var1 = verify(node.children[board[i][j]],i+1,j,visited)
                var3 = verify(node.children[board[i][j]],i,j+1,visited)
                var2 = verify(node.children[board[i][j]],i-1,j,visited)
                var4 = verify(node.children[board[i][j]],i,j-1,visited)
                visited.remove((i,j))
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                verify(root, i , j,set())
        return list(res)