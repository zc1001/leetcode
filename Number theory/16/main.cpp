/*
˫ָ��
д�ú�ӷ��
ִ����ʱ :520 ms, ������ C++ �ύ�л�����5.01% ���û�
�ڴ����� :8.8 MB, ������ C++ �ύ�л�����73.45%���û�
*/
#include <iostream>
#include <vector>
#include <algorithm>
 #include <cstdlib>
using namespace std;
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
       sort(nums.begin(),nums.end());
       int min_num = 10000;
       for(int i=1;i<nums.size()-1;i++)
       {
           int l =0;
           int r = nums.size()-1;
           while(l<r)
           {
              // cout<<l<<" "<<i<<" "<<r<<endl;
               if(abs(nums[i]+nums[l]+nums[r]-target)<abs(min_num))
                 min_num = nums[i]+nums[l]+nums[r]-target;
               if(abs(nums[i]+nums[l]+nums[r]-target) == 0)
               {
                   //cout<<"ok"<<endl;
                   min_num = nums[i]+nums[l]+nums[r]-target;
                   break;
               }

               if(l == r-2)
                break;
               if(l+1<=i&&r-1>i)
                   r--;
                else
                if(l+1 < i && r-1==i)
                {
                   r = nums.size()-1;
                   l++;
                }




           }

       }
       return min_num + target;
    }
};
int main()
{
    int b[] = {-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33};
    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    Solution p;
    int tup  = p.threeSumClosest(vecHeight,0);
    cout<<tup<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
