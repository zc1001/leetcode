#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        vector<int> opt;
        opt.push_back(1);
        opt.push_back(2);
        opt.push_back(3);
        if(n <=3)
            return opt[n-1];
        else
        {
            for(int i=3;i<n;i++)
            {
                opt.push_back(opt[i-1] + opt[i-2]);

            }
            return opt[opt.size()-1];
        }
    }
};
int main()
{
      int b[] = {10, 15, 20};
    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    Solution sol;
    int num = sol.climbStairs(15);
    cout<<num<<endl;
    vector<int> d;
    vector<int> q;
    cout << "Hello world!" << endl;
    return 0;
}
