class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int,int>> speedCar;
        for(int i = 0; i < speed.size() ; i++){
            speedCar.push_back( {position[i],speed[i]});
        }
        std::sort(speedCar.begin(),speedCar.end());
        std::stack<double> fleet;
        for(int i = speedCar.size() - 1; i >= 0 ; i--){
            double time = 
            (double)(target - speedCar[i].first)/(double)speedCar[i].second;
            if(fleet.empty() || fleet.top() < time){
                fleet.push(time);
            }
        }
        return fleet.size();

    }
};
