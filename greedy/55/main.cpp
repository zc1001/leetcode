/*
greedy
���ù�������
��ͷ��ʼ���� ֻҪ�ҵ�0���Ϳ�����0�ĸ�����Ȼ��Ӻ���ǰ����û�п����ľ������0�ĸ���+��һ���㵽�˵�ľ�������û��������
ִ����ʱ :20 ms, ������ C++ �ύ�л�����38.89% ���û�
�ڴ����� :9.6 MB, ������ C++ �ύ�л�����99.57%���û�
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
