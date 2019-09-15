/*
greedy
不用管其他的
从头开始遍历 只要找到0，就看连续0的个数，然后从后往前找有没有可跳的距离大于0的个数+第一个零到此点的距离的如果没有跳不到
执行用时 :20 ms, 在所有 C++ 提交中击败了38.89% 的用户
内存消耗 :9.6 MB, 在所有 C++ 提交中击败了99.57%的用户
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int i=0;
        bool f = true;
        if(nums.size() == 0)
            return false;
        if(nums.size() == 1)
            return true;
        if(nums[0] == 0)
            return false;
        while(i<nums.size()-1)
        {
            int len = 0;
         if(nums[i] != 0)
            i++;
         else
         {
             len = 0;
             while(i<nums.size()-1&&nums[i] == 0)
             {
                 len++;
                 i++;
             }
        bool flage = false;
         for(int j = i-len-1;j>=0;j--)
         {
             if(nums[j]>=(i-j))
                flage = true;
         }
         if(flage == false)
            f = false;
         }

        }
        return f;
    }
};
int main()
{
      int b[] ={2,0,0};
    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    Solution u;
    bool g = u.canJump(vecHeight);
    cout<<g<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
