class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
            9: set()
        }
        colMap = {
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
            9: set()
        }
        sqrMap = {
            (0,0): set(),
            (0,1): set(),
            (0,2): set(),
            (1,0): set(),
            (1,1): set(),
            (1,2): set(),
            (2,0): set(),
            (2,1): set(),
            (2,2): set()
        }
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowMap[i+1]:
                    return False
                if board[i][j] in colMap[j+1]:
                    return False
                if board[i][j] in sqrMap[(int(i/3),int(j/3))]:
                    return False
                rowMap[i+1].add(board[i][j])
                colMap[j+1].add(board[i][j])
                sqrMap[(i//3,j//3)].add(board[i][j])
                
            

        return True
        