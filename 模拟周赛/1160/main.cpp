#include <iostream>
#include <string.h>
#include <vector>
using namespace std;
class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int arr[200];
        //memset(arr,0,sizeof(arr));
        for(int i=0;i<200;i++)
            arr[i] = 0;
        int length = 0;
        for(int i=0;i<chars.length();i++)
        {
            arr[((int)chars[i])]++;
        }
        for(int i=0;i<words.size();i++)
        {
            bool flage = true;
            for(int j=0;j<words[i].length();j++)
            {
                if(arr[(int)words[i][j]] == 0)
                    flage = false;
            arr[(int)words[i][j]]--;
            }
            if(flage == true)
            {

            length += words[i].length();
            }
             for(int j=0;j<words[i].length();j++)
            {
               arr[(int)words[i][j]]++;
            }
        }
      return length;
    }
};
int main()
{
    string b[] = {"cat","bt","hat","tree"};
    vector<string> vecHeight(b, b+sizeof(b)/sizeof(int));
    string chas = "atach";
    Solution sol;
    int num = sol.countCharacters(vecHeight,chas);
    cout<<num<<endl;
    cout<<(int)('a')<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
