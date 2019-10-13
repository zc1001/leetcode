/*
大神的想法
dp
//使用dp数组，dp[i]代表组合数为i时使用nums中的数能组成的组合数的个数
//dp[i]=dp[i-nums[0]]+dp[i-nums[1]]+dp[i=nums[2]]+...
        //举个例子比如nums=[1,3,4],target=7;
        //dp[7]=dp[6]+dp[4]+dp[3]
        //其实就是说7的组合数可以由三部分组成，1和dp[6]，3和dp[4],4和dp[3];
执行用时 :4 ms, 在所有 C++ 提交中击败了84.97% 的用户
内存消耗 :8.6 MB, 在所有 C++ 提交中击败了60.32%的用户

*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned int> opt;
        opt.push_back(1);
        sort(nums.begin(),nums.end());
        for(int i=1;i<=target;i++)
        {
            unsigned int num = 0;
            for(int j=0;j<nums.size();j++)
            {
                if(i<nums[j])
                    break;
                num += opt[i - nums[j]];
            }

            opt.push_back(num);
        }
        return opt[opt.size()-1];
    }
};
int main()
{
    int b[] = {3,33,333};

    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    Solution r;
    int c = r.combinationSum4(vecHeight,10000);
    cout<<c<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
