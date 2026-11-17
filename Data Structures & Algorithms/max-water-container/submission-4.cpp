class Solution {
public:
    int maxArea(vector<int>& heights) {
        int i = 0 , j = heights.size()-1 ;
        int res=0;
        while( i < heights.size() && j < heights.size()){
            res = std::max(res,(std::min(heights[i],heights[j])) * (j-i));
            if(heights[i] < heights[j]){
                i++;
            }else {
                j--;
            }
            
        }
        return res;
    }
};
