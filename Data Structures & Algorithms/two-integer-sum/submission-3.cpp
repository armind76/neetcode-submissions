class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> check;
        for(int i = 0; i < nums.size(); i++){
            if(check.find(nums[i]) == check.end()){
                check[target-nums[i]] = i + 1;
            }else{
                return {check[nums[i]]-1,i};
            }
        }
    }
};
