class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<int> res;
        for(auto n: nums){
            count[n]++;
        }
        vector<pair<int,int>> arr;
        for(auto & p: count){
            arr.push_back({p.second,p.first});
        }
        sort(arr.rbegin(), arr.rend());

        for(int i = 0 ; i < k ; i++){
            res.push_back(arr[i].second);
        }

        return res;

        
    }
};
