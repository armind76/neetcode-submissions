class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0 || nums.size() == 1){
            return nums.size();
        }
        std::sort(nums.begin(),nums.end());
        int res = 0, count =0;
        for(int i = nums.size() ; i >= 1 ; i--){
            if(nums[i] == nums[i-1] + 1){
                count ++;
                res = std::max(count, res);
            }else if(nums[i]==nums[i-1]){

            }
            else{
                count = 0;
            }
        }
        return res + 1;
    }
};
