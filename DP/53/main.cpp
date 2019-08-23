#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int start = 0;
        int end = 0;
        vector<int> opt;
        opt.push_back(nums[0]);
        if(nums.size() ==1)
            return nums[0];
        if(nums[1] > 0&&nums[0]>0)
        {
           // cout<<5<<endl;
            opt.push_back(nums[1]+nums[0]);
            start = 0;
            end = 1;
        }
        else
        {
            if(nums[1]>=nums[0])
            {
               opt.push_back(nums[1]);
               start = 1;
               end = 1;
            }
            else
                opt.push_back(nums[0]);
        }
           // opt.push_back(nums[0]);
        for(int i=2;i<nums.size();i++)
        {

                int num = 0;
                int max = -1100000;
                int local = end;
                for(int j = i;j>=start;j--)
                {
                    num += nums[j];
                    if(num>max)
                    {
                       // cout<<num<<"  "<<max<<endl;
                        max = num;
                        local = j;

                    }

                }

                if(max>=opt[end])
                {
                    opt.push_back(max);
                    //cout<<max<<endl;
                    start = local;
                    end = i;
                }
                else
                    opt.push_back(opt[end]);
                   // cout<<start<<"   "<<end<<endl;


        }

        return opt[opt.size()-1];
    }
};
int main()
{
    int b[] = {3,1,0,1};
    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    Solution sol;
    int num = sol.maxSubArray(vecHeight);
    cout<<num<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
