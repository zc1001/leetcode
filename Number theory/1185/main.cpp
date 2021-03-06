/*
菜勒公式
直接暴力
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
       string weeks[7] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
        int month_days[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
        // 1971-01-01 星期五
        int sum = 0;
        for(int i=1971; i<year; i++)
        {
            if( (i % 4 ==0 && i % 100 != 0) || (i % 400 == 0) )
                sum += 366;
            else
                sum += 365;
        }
        for(int i=0; i<month-1; i++)
        {
            sum += month_days[i];
            if(i == 1 && ((year % 4 ==0 && year % 100 != 0) || (year % 400 == 0)))
                sum += 1;
        }
        sum += day;
        return weeks[(sum + 4) % 7];
    }
};
int main()
{
    Solution w;
    string u = w.dayOfTheWeek(18,7,1999);
    cout<<u<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
