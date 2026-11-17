class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<int> res;
        for(auto n: nums){
            count[n]++;
        }
        priority_queue<pair<int,int>> pq;
        for(auto &c: count){
            pq.push({c.second,c.first});
        }
        for(int i = 0; i < k ; i++){
            res.push_back(pq.top().second);
            pq.pop();
        }

        return res;
    }
};
