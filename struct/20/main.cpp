/*\
ջ ����
ִ����ʱ :8 ms, ������ C++ �ύ�л�����33.89% ���û�
�ڴ����� :8.6 MB, ������ C++ �ύ�л�����69.52%���û�
*/
#include <iostream>
#include <vector>
#include <stack>
using namespace std;
class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        for(int i=0;i<s.length();i++)
        {
            switch(s[i])
            {
           case '(' :
            st.push(s[i]);
            break;
           case '{':
            st.push(s[i]);
            break;
           case '[':
            st.push(s[i]);
            break;
           case ')':
            if(st.size()>0&&st.top() == '(')
            {
                st.pop();
            }
            else
                return false;
            break;
           case '}':
            if(st.size()>0&&st.top() == '{')
            {
                st.pop();
            }
            else
                return false;
            break;
           case ']':
            if(st.size()>0&&st.top() == '[')
            {
                st.pop();
            }
            else
                return false;
            break;
            }
        }
        if(st.size() == 0)
            return true;
        else
            return false;
    }
};
int main()
{
    Solution u;
    bool a = u.isValid("]");
    cout<<a<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
