class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string,vector<string>> result;
        for(auto s: strs){
            vector<int> count(26,0);
            for(auto c : s){
                count[c-'a']++;
            }
            string key = "";
            for(auto i: count){
                key += i;
            }
            result[key].push_back(s);

        }
        vector<vector<string>> toReturn;
        for (auto r: result){
            toReturn.push_back(r.second);
        }
        return toReturn;
    }
};
