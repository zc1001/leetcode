#include <iostream>
#include <string.h>
using namespace std;
class Solution {
public:
    string convertToTitle(int n) {
        string s = "";
        char c;
        while(n)
        {
            c = (n-1)%26 + 'A';
            s = c + s;
            n = (n-1)/26;
        }
        return s;
    }
};
int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
