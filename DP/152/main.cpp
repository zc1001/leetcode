#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max = -1000;
        vector<int> zheng;
        vector<int> f;
        vector<int> opt;
        if(nums[0]>0)
        {
            zheng.push_back(nums[0]);
            f.push_back(0);
        }
        else
        {
            f.push_back(nums[0]);
            zheng.push_back(0);
        }
        max = nums[0];
        opt.push_back(max);
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i]>0)
            {
                if(zheng[i-1] == 0)
                    zheng.push_back(nums[i]);
                else
                    zheng.push_back(zheng[i-1]*nums[i]);
                f.push_back(nums[i]*f[i-1]);

            }
            if(nums[i]<0)
            {
                if(f[i-1]==0)
                {
                    if(zheng[i-1] != 0)
                        f.push_back(nums[i]*zheng[i-1]);
                    else
                        f.push_back(nums[i]);
                    zheng.push_back(0);

                }
                else
                {
                    zheng.push_back(f[i-1]*nums[i]);
                    if(zheng[i-1] != 0)
                      f.push_back(nums[i]*zheng[i-1]);
                    else
                        f.push_back(nums[i]);
                }
            }
             if(nums[i] == 0)
                {
                    zheng.push_back(0);
                    f.push_back(0);
                }
            }
            for(int i=0;i<zheng.size();i++)
            {
                if(zheng[i] == 0)
                    zheng[i] = 1;
                if(f[i] == 0)
                    f[i] = 1;
            }
            for(int i=1;i<nums.size();i++)
            {
                if(nums[i]>0)
                {
                    if((nums[i]*zheng[i-1])>opt[i-1])
                        opt.push_back(nums[i]*zheng[i-1]);
                    else
                        opt.push_back(opt[i-1]);
                }
                if(nums[i]<0)
                {
                    if((nums[i]*f[i-1])>opt[i-1])
                        opt.push_back(nums[i]*f[i-1]);
                    else
                        opt.push_back(opt[i-1]);
                }
                if(nums[i] == 0)
                {
                    if(nums[i]>opt[i-1])
                        opt.push_back(nums[i]);
                    else
                        opt.push_back(opt[i-1]);
                }
            }
            for(int i=0;i<zheng.size();i++)
            {
                cout<<zheng[i]<<"             "<<f[i]<<endl;
            }
            return opt[opt.size()-1];
        }



};
int main()
{
     int b[] = {2,-5,-2,-4,3};
    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    Solution s;
    int a = s.maxProduct(vecHeight);
    cout<<a<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
