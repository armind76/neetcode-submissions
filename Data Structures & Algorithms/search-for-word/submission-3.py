class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i,j, charIndx):

            if i<0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[charIndx] != board[i][j]:
                return False            
            
            if charIndx == len(word)-1:
                
                return True

            tmp = board[i][j]
            board[i][j] = "#"
            r = backtrack(i+1, j, charIndx+1) or backtrack(i-1, j, charIndx+1)or backtrack(i, j+1, charIndx+1) or backtrack(i, j-1, charIndx+1)
            board[i][j] = tmp
            return r
        if not board:
            return word == ""

        for i in range(len(board)):
            for j in range(len(board[0])):

                res = backtrack(i,j,0)
                if res:
                    return True
        return False

            