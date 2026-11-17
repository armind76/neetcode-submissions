class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stck;
        std::unordered_map<char,char> map = 
        {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        for(auto c: s){
            if(!map.count(c)){
                stck.push(c);
            }
            else if (!stck.empty() && map[c] == stck.top()){
                stck.pop();
            }
            else
            {
                return false;
            }

        }
        return stck.empty();


    }
};
