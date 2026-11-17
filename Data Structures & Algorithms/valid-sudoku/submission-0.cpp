class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> col,row;
        map<pair<int,int>,unordered_set<char>> box;
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9 ; j ++){
                if(board[i][j] == '.') continue;
                pair<int,int> key ={i /3 , j/3};
                if(row[i].find(board[i][j]) != row[i].end() || col[j].find(board[i][j]) != col[j].end()
                || box[key].find(board[i][j]) != box[key].end()){
                    return false;
                }
                else{
                    row[i].insert(board[i][j]);
                    col[j].insert(board[i][j]);
                    box[key].insert(board[i][j]);
                }

            }
        }
        return true;
    }
};
