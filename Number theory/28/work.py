import  math

# 直接return
#执行用时 :20 ms, 在所有 Python 提交中击败了84.85% 的用户
# 内存消耗 :12.2 MB, 在所有 Python 提交中击败了12.67%的用户

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle);


if __name__ == '__main__':
    p = Solution()
    print(p.strStr("aaaaaaa","ll"))





    #print(s)
    #print(test.lastSubstring("abab"))
