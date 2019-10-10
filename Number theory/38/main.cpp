/*
 * 直接暴力
 * 刚换的位置 做个简单的
 * 执行用时 :4 ms, 在所有 C++ 提交中击败了91.30% 的用户
内存消耗 :8.7 MB, 在所有 C++ 提交中击败了73.16%的用户
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
    string countAndSay(int n) {
        vector <string> v;
        string str = "1";
        //v.push_back(str);
        if(n>1)
        for(int i=2;i<=n;i++)
        {
            int j = 0;
            string newstr = "";
            int count = 1;
            while(j < str.length())
            {
                if(str[j] == str[j+1])
                {
                    count++;
                   // j++;
                }
                else
                {
                    newstr += to_string(count);
                    newstr += str[j];
                    count = 1;
                }
                j++;
            }
            str  = newstr;
        }
        return str;
    }
};
int main()
{
    Solution s;
    string a = s.countAndSay(4);
    cout<<a<<endl;
   return 0;
}
