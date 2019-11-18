# 执行用时 :16 ms, 在所有 python 提交中击败了89.18% 的用户
# 内存消耗 :11.8 MB, 在所有 python 提交中击败了35.18%的用户
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        S = s.split()
        if(len(S) == 0):
            return 0
        else:
            return len(S[len(S)-1])










if __name__ == '__main__':
    p = Solution()
    n1 = [1,2,3,0,0,0]
    n2 = [2,5,6]
    d = p.merge(n1,3,n2,3)
    print(d)

