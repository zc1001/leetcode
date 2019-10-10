/*
 * 二分
 * 哈哈哈哈 最近很喜欢做简单的题 但是 这个还没有1A😌
 * 执行用时 :8 ms, 在所有 C++ 提交中击败了79.84% 的用户
内存消耗 :8.9 MB, 在所有 C++ 提交中击败了77.90%的用户
 *
 * */
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
#include <string>
using namespace std;
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
      int min = 0;
      int max = nums.size()-1;
      if(target > nums[nums.size()-1])
          return nums.size();
      if(target < nums[0])
          return 0;
      while(min<=max)
      {
          int h = (max + min)/2;
          if(nums[h] == target  )
              return h;
          if(nums[h] > target)
          {
              if(nums[h-1]<target)
                  return h;
              else
              max = h-1;
          }
          else
          {
              if(nums[h+1] > target)
                  return h+1;
              else
              min = h+1;
          }

      }
      return 0;
    }
};
int main()
{
    Solution s;
    int arrHeight[] = {1,3,5,6};
    vector<int> vecHeight(arrHeight, arrHeight+sizeof(arrHeight)/sizeof(float));
    int a = s.searchInsert(vecHeight,7);
    cout<<a<<endl;
   return 0;
}
