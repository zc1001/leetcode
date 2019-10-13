/*
����һ������ һֱ��һ
�ڶ�����������
Ȼ���
ִ����ʱ :8 ms, ������ C++ �ύ�л�����77.45% ���û�
�ڴ����� :9.4 MB, ������ C++ �ύ�л�����75.66%���û�
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = 1;
        int rmin = 0;
        int rmax = numbers.size()-1;
        vector <int> c;
        while(l<numbers.size())
        {
            r = (rmax +rmin)/2;
            // cout<<l<<"  "<<r<<endl;
            if(numbers[l] + numbers[r] == target)
            {
                c.push_back(l);
                c.push_back(r);

                return c;
            }
            if(numbers[l] + numbers[r] > target)
            {
                rmax = r-1;
            }
            if(numbers[l] + numbers[r] < target)
            {
                rmin = r+1;
            }
            if(rmin > rmax)
            {
                l++;
                rmin = l+1;
                rmax = numbers.size()-1;
            }

        }

    }
};
int main()
{
    int b[] = {2,3,4};

    vector<int> vecHeight(b, b+sizeof(b)/sizeof(int));
    Solution r;
    vector <int> c;
    c = r.twoSum(vecHeight,6);
    cout<<c[0]<<c[1]<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
