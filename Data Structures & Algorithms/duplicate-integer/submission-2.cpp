class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int , int> dupe;
        for(auto i: nums){
            if(dupe[i] != 1){
                dupe[i]++;
            }else
                return true;
        }
        return false;
    }
};
