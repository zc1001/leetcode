/*
暴力
1A
执行用时 :8 ms, 在所有 C++ 提交中击败了57.22% 的用户
内存消耗 :8.2 MB, 在所有 C++ 提交中击败了28.17%的用户
*/
#include <iostream>
#include <string.h>
using namespace std;
class Solution {
public:
    int titleToNumber(string s) {
        int sum = 0;
        for(int i=0;i<s.length();i++)
        {
           int num = s[i] -64;
           //cout<<num<<endl;
           for(int j = 0;j<s.length()-i-1;j++)
            num *= 26;
           sum += num;
        }
        return sum;
    }
};
int main()
{
    cout << "Hello world!" << endl;
    Solution s;
    cout<<s.titleToNumber("AB");
    return 0;
}
