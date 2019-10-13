/*
 * 暴力
 * 三次循环
 * 第一次把nums1的数字变成下标存在数组里然后遍历nums2，找到相等的数字变成下标存在另一个数组
 * 遍历数组，找到不为0的下标，然后就直接存到vector里
 *
 *
 * 执行用时 :24 ms, 在所有 cpp 提交中击败了15.91%的用户
* 内存消耗 :9.8 MB, 在所有 cpp 提交中击败了6.71%的用户
 * */
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
#include <string>
using namespace std;
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int com[100010];
        int com2[100010];
        vector <int> c;
        memset(com,0, sizeof(com));
        memset(com2,0, sizeof(com2));
        for(int i=0;i<nums1.size();i++)
            com[nums1[i]] += 1;
        sort(nums2.begin(),nums2.end());
        for(int i=0;i<nums2.size();i++)
        {
            if(com[nums2[i]]>0)
                com2[nums2[i]]++;
        }
        for(int i = 0;i<100010;i++)
            if(com2[i]>0)
                c.push_back(i);
        return c;


    }
};
int main()
{
    Solution s;
    int arrHeight[] = {1,2,2,1};
    vector<int> vecHeight(arrHeight, arrHeight+sizeof(arrHeight)/sizeof(float));
    int arrHeight2[] = {2,2};
    vector<int> vecHeight2(arrHeight2, arrHeight2+sizeof(arrHeight2)/sizeof(float));
    vector <int> a = s.intersection(vecHeight,vecHeight2);
    for(int i=0;i<a.size();i++)
        cout<<a[i]<<" ";
   return 0;
}
