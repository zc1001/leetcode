/*
ֱ�Ӷ���
����
ִ����ʱ :0 ms, ������ cpp �ύ�л�����100.00% ���û�
�ڴ����� :8.2 MB, ������ cpp �ύ�л�����21.13%���û�
*/
#include <iostream>

using namespace std;
class Solution {
public:
    int firstBadVersion(int n) {
        long long int r = n;
        long long int l = 1;
        while(l<r)
        {
            long long int h = (l+r)/2;
            bool a = isBadVersion(h);
            bool b = isBadVersion(h-1);
            bool c = isBadVersion(h+1);
            if(a && !b)
                return h;
            if(!a && c)
                return h+1;
            if(a)
                r = h-1;
            else
                l = h+1;

        }
        return 1;
    }
};
int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
