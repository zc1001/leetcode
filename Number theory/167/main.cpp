/*
控制一个变量 一直加一
第二个变量二分
然后就
执行用时 :8 ms, 在所有 C++ 提交中击败了77.45% 的用户
内存消耗 :9.4 MB, 在所有 C++ 提交中击败了75.66%的用户
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = 1;
        int rmin = 0;
        int rmax = numbers.size()-1;
        vector <int> c;
        while(l<numbers.size())
        {
            r = (rmax +rmin)/2;
            // cout<<l<<"  "<<r<<endl;
            if(numbers[l] + numbers[r] == target)
            {
                c.push_back(l);
                c.push_back(r);

                return c;
            }
            if(numbers[l] + numbers[r] > target)
            {
                rmax = r-1;
            }
            if(numbers[l] + numbers[r] < target)
            {
                rmin = r+1;
            }
            if(rmin > rmax)
            {
                l++;
                rmin = l+1;
                rmax = numbers.size()-1;
            }

        }

    }
};
int main()
{
    int b[] = {2,3,4};

    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    Solution r;
    vector <int> c;
    c = r.twoSum(vecHeight,6);
    cout<<c[0]<<c[1]<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
