/*
����
1A
ִ����ʱ :8 ms, ������ C++ �ύ�л�����57.22% ���û�
�ڴ����� :8.2 MB, ������ C++ �ύ�л�����28.17%���û�
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
