/*
map
暴力
执行用时 :40 ms, 在所有 C++ 提交中击败了49.68% 的用户
内存消耗 :11.5 MB, 在所有 C++ 提交中击败了5.12%的用户
*/
#include <iostream>
#include <vector>
#include <map>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
       map <int,int> num;
       for(int i=0;i<nums.size();i++)
            num[nums[i]] = 1;
    nums.clear();
       map<int,int>::iterator map_iter = num.begin();
       for(map_iter = num.begin();map_iter != num.end();map_iter++)
        nums.push_back(map_iter->first);
       return num.size();
    }
};
int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
