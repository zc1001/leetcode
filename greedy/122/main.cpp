/*
贪心
min = prices[0]
for i in range（size of prices）
    if prices[i]<=prices[i-1]
       总价格 + prices[i] -min
       min = prices[i]
    end if
return 总价格
执行用时 :8 ms, 在所有 C++ 提交中击败了84.40% 的用户
内存消耗 :9.4 MB, 在所有 C++ 提交中击败了70.90%的用户
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() == 0 || prices.size() == 1)
            return 0;
        int price = 0;
        int day_price = prices[0];
        int min = prices[0];

        if(prices.size() == 2)
        {
            int num = prices[1] - prices[0];
            if(num<0)
            return 0;
            else
                return num;
        }

        for(int i=1;i<prices.size();i++)
        {
            if(prices[i]<=day_price)
            {
                price += prices[i-1] - min;
                min = prices[i];
            }

                day_price = prices[i];
            //cout<<price<<endl;
        }
        if(prices[prices.size()-1]>prices[prices.size()-2])
            price += prices[prices.size()-1] - min;
        return price;
    }
};
int main()
{
       int b[] = {};
    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    int c;
    Solution t;
    c = t.maxProfit(vecHeight);
    cout<<c<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
