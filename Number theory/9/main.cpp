/*
����
ִ����ʱ :56 ms, ������ C++ �ύ�л�����5.58% ���û�
�ڴ����� :8.1 MB, ������ C++ �ύ�л�����84.18%���û�
*/
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
class Solution {
public:
    bool isPalindrome(int x) {
        stringstream ss;
       ss << x;
       string str = ss.str();
       bool flage = true;
       if(str.length()%2 ==0)
       {
           for(int i=0;i<str.length()/2;i++)
       {
           if(str[i] != str[str.length()-1-i])
           {
               flage = false;
               break;
           }
       }
       }
       else
       {
           for(int i=0;i<(str.length()-1)/2;i++)
           {
               if(str[i] != str[str.length()-1-i])
           {
               flage = false;
               break;
           }
           }
       }
       return flage;

    }
};
int main()
{
    Solution d;
    bool f = d.isPalindrome(123);
    cout<<f<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
