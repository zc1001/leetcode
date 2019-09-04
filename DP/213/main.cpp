/*
DP
和198 相似
做两次DP
第一次不包括nums[0]
第二次不包括nums[nums.size()-1]
找最大的值
执行用时 :4 ms, 在所有 C++ 提交中击败了79.40% 的用户
内存消耗 :8.7 MB, 在所有 C++ 提交中击败了73.26%的用户
*/
#include <iostream>
#include <vector>
#include <algorithm>
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
    if(nums.size() == 3)
    {
        if(max(nums[0],nums[1])>nums[2])
            return max(nums[0],nums[1]);
        else
           return nums[2];
    }
    int max1;
    int max2;
    vector<int> opt;
    opt.push_back(nums[0]);
    if(nums[0]>nums[1])
        opt.push_back(nums[0]);
    else
        opt.push_back(nums[1]);
    for(int i=2;i<nums.size()-1;i++)
    {
        if((opt[i-2]+nums[i])>opt[i-1])
            opt.push_back(opt[i-2]+nums[i]);
        else
            opt.push_back(opt[i-1]);
    }
    max1 = opt[opt.size()-1];
    vector<int> num;
    for(int i=1;i<nums.size();i++)
        num.push_back(nums[i]);
    opt.clear();
    opt.push_back(num[0]);
    if(num[0]>num[1])
        opt.push_back(num[0]);
    else
       opt.push_back(num[1]);
    for(int i=2;i<num.size();i++)
    {
        if((opt[i-2]+num[i])>opt[i-1])
        {
            //cout<<opt[i-2]+nums[i]<<endl;
            opt.push_back(opt[i-2]+num[i]);
        }
        else
            opt.push_back(opt[i-1]);
    }
      //for(int i=0;i<opt.size();i++)
       // cout<<opt[i]<<endl;
    max2 = opt[opt.size()-1];
    //cout<<max1<<" "<<max2<<endl;
    if(max1>max2)
        return max1;
    else
        return max2;

    }
};
int main()
{    int b[] = {2,2,4,3,2,5};
    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    Solution ch;
    int l = ch.rob(vecHeight);
    cout<<l<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
