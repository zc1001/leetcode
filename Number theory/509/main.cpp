#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int fib(int N) {
        vector<int> f;
        f.push_back(0);
        f.push_back(1);
        if(N<=2)
            return f[N];
        else{
            for(int i=2;i<=N;i++)
                f.push_back(f[i-1] + f[i-2]);
            return f[f.size()-1];
        }

    }
};
int main()
{
    Solution so;
    int a = so.fib(2);
    cout<<a<<endl;
    return 0;
}
