/*
直接二分
手敲
执行用时 :0 ms, 在所有 cpp 提交中击败了100.00% 的用户
内存消耗 :8.2 MB, 在所有 cpp 提交中击败了21.13%的用户
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
