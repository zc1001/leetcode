/*
greedy
ֱ��sort��Ȼ���С���ж�
���ϼ������Ǽ���
ִ����ʱ :72 ms, ������ C++ �ύ�л�����35.56% ���û�
�ڴ����� :10.4 MB, ������ C++ �ύ�л�����44.59%���û�
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        int count = 0;

            int i=0;
            int j=0;
         while(i<g.size()&&j<s.size())
         {
             if(s[j]>=g[i])
             {
                 j++;
                 i++;
                 count++;
             }
            else
            {
                j++;
            }
         }
        return count;
    }
};
int main()
{
    int b[] ={1,2};
    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    int c[] ={1,2,3};
    vector<int> vecHeightg(c, c+sizeof(c)/sizeof(int));
    int y;
    Solution p;
    y = p.findContentChildren(vecHeight,vecHeightg);
    cout<<y<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
