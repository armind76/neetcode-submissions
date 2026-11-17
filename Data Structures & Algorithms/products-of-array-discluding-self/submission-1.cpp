class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
      vector<int> res(nums.size(), 0);
      int prod = 1, zeroCount = 0;
      for(int n:nums){
        if(n != 0){
            prod *= n;
        }else
            zeroCount++;
      }
      if(zeroCount > 1){
        return res;
      }
      else if(zeroCount == 0)
      {
        for(int i = 0; i < nums.size();i++){    
                res[i] = prod / nums[i];
        }
      }
      else
      {
        for(int i = 0; i < nums.size();i++){    
            if(nums[i] == 0)
                res[i] = prod;
        } 
      }
    }
};
