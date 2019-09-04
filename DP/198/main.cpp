/*
DP
opt[i] i 的时候小偷最多能投多少钱
opt[i] =
if(opt[i-2]+nums[i])>opt[i-1]
    opt[i] = opt[i-2] +nums[i]
else
    opt[i] = opt[i-1]

*/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int rob(vector<int>& nums) {
    if(nums.size() == 0)
       return 0;
    if(nums.size() == 1)
        return nums[0];
    if(nums.size() == 2)
    {
        if(nums[0]>nums[1])
            return nums[0];
        else
            return nums[1];
    }
    vector<int> opt;
    opt.push_back(nums[0]);
    if(nums[0]>nums[1])
        opt.push_back(nums[0]);
    else
        opt.push_back(nums[1]);
    for(int i=2;i<nums.size();i++)
    {
        if((opt[i-2]+nums[i])>opt[i-1])
            opt.push_back(opt[i-2]+nums[i]);
        else
            opt.push_back(opt[i-1]);
    }

     return opt[opt.size()-1];
    }
};
int main()
{

     int b[] = {2,7,9,3,1};
    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    Solution t;
    int k = t.rob(vecHeight);
    cout<<k<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
