/*
虽然是dp 但是暴力通过
*/

#include <iostream>
#include <vector>
#include <map>
using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
       int max = 0;
       int min = 1000000;
       if(prices.size()<3)
       {
        if(prices.size() ==2)
        if(prices[1]-prices[0] >0)
           {
               int a = prices[1] -prices[0];
               return a;
           }
         return max;
       }
       if(prices[1]-prices[0] >0)
           {
               max = prices[1] - prices[0];
               min = prices[0];
           }
        else
            min = prices[1];
       for(int i=2;i<prices.size();i++)
       {
           if(prices[i]<min)
            min = prices[i];
           else{
            if((prices[i] - min >max))
                max = prices[i] - min;
           }
       }
       return max;
    }
};
int main()
{
    int b[] = {};
    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    int w;
    Solution s;
    w = s.maxProfit(vecHeight);
    cout<<w<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
