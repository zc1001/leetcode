#include <iostream>
#include <vector>
#include <map>
using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
       for(int i=0;i<prices.size();i++)
       {
           for(int j = i;j<prices.size();j++)
           {
               if(prices[j] - prices[i] >max)
                max = prices[j] - prices[i];
           }

       }
       return max;
    }
};
int main()
{
    int b[] = {7,1,5,3,6,4};
    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    int w;
    Solution s;
    w = s.maxProfit(vecHeight);
    cout<<w<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
