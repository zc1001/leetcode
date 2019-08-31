/*
̰��
min = prices[0]
for i in range��size of prices��
    if prices[i]<=prices[i-1]
       �ܼ۸� + prices[i] -min
       min = prices[i]
    end if
return �ܼ۸�
ִ����ʱ :8 ms, ������ C++ �ύ�л�����84.40% ���û�
�ڴ����� :9.4 MB, ������ C++ �ύ�л�����70.90%���û�
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
