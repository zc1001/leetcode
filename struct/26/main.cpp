/*
map
����
ִ����ʱ :40 ms, ������ C++ �ύ�л�����49.68% ���û�
�ڴ����� :11.5 MB, ������ C++ �ύ�л�����5.12%���û�
*/
#include <iostream>
#include <vector>
#include <map>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
       map <int,int> num;
       for(int i=0;i<nums.size();i++)
            num[nums[i]] = 1;
    nums.clear();
       map<int,int>::iterator map_iter = num.begin();
       for(map_iter = num.begin();map_iter != num.end();map_iter++)
        nums.push_back(map_iter->first);
       return num.size();
    }
};
int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
