#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> opt0;
        vector<int> opt1;
        vector<bool> choose;
        opt0.push_back(cost[0]);
        opt1.push_back(cost[0]);
        opt0.push_back(cost[1]);
        opt1.push_back(cost[0]);
        for(int i=2;i<cost.size();i++)
        {
            int num = 0;
          if((opt0[i-1]+cost[i])<=(opt0[i-2]+cost[i]))
            num = opt0[i-1]+cost[i];
          else
            num = opt0[i-2]+cost[i];
          if((opt1[i-1]+cost[i-1]+cost[i])<=(opt1[i-2]+cost[i-2]+cost[i]))
          {
              if(num>(opt1[i-1]+cost[i-1]+cost[i]))
                num = (opt1[i-1]+cost[i-1]+cost[i]);
          }
          else
            if(num > (opt1[i-2]+cost[i-2]+cost[i]))
            num = (opt1[i-2]+cost[i-2]+cost[i]);
         opt0.push_back(num);
         opt1.push_back(opt0[i-1]);
         cout<<num<<endl;
        }
        if(opt0[opt0.size()-1]<opt1[opt1.size()-1])
             return opt0[opt0.size()-1];
        else
            return opt1[opt1.size()-1];

    }
};
int main()
{
      int b[] = {10, 15, 20};
    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    Solution sol;
    int num = sol.minCostClimbingStairs(vecHeight);
    cout<<num<<endl;
    vector<int> d;
    vector<int> q;
    cout << "Hello world!" << endl;
    return 0;
}
