/*
������뷨
dp
//ʹ��dp���飬dp[i]���������Ϊiʱʹ��nums�е�������ɵ�������ĸ���
//dp[i]=dp[i-nums[0]]+dp[i-nums[1]]+dp[i=nums[2]]+...
        //�ٸ����ӱ���nums=[1,3,4],target=7;
        //dp[7]=dp[6]+dp[4]+dp[3]
        //��ʵ����˵7���������������������ɣ�1��dp[6]��3��dp[4],4��dp[3];
ִ����ʱ :4 ms, ������ C++ �ύ�л�����84.97% ���û�
�ڴ����� :8.6 MB, ������ C++ �ύ�л�����60.32%���û�

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
