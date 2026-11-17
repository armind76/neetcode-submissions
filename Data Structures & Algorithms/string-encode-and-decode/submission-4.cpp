class Solution {
//2#aa

public:

    string encode(vector<string>& strs) {
        string encoded = "" ;
        for(auto s: strs){
            encoded = encoded + to_string(s.size()) + '#' + s;
        }
        return encoded;

    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        while(i < s.size()){
            int j = i;
            while(s[j] != '#'){
                j++;
            }
            int length = stoi(s.substr(i, j - i));
            i = j+1;
            res.push_back(s.substr(i ,length));
            i += length;
        }
        return res;
    }
};
