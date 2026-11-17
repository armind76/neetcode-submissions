class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map <char, int> mps,mpt;
        if(s.length() != t.length()){
            return false;
        }
        for(int i = 0 ; i < t.length();i++){
            mps[s[i]]++;
            mpt[t[i]]++;
        }
        return (mps == mpt);
    }
};
