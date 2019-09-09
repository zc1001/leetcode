/*\
栈 暴力
执行用时 :8 ms, 在所有 C++ 提交中击败了33.89% 的用户
内存消耗 :8.6 MB, 在所有 C++ 提交中击败了69.52%的用户
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
