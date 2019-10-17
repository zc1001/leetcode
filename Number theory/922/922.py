import  math

#  python 可暴力
# 执行用时 :208 ms, 在所有 python 提交中击败了87.86% 的用户
# 内存消耗 :13.9 MB, 在所有 python 提交中击败了19.72%的用户
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = []
        o = []
        c = []
        for i in A:
            if(i%2 ==0 ):
                o.append(i)
            else:
                j.append(i)
        i = 0
        while(i < len(j)):
            c.append(o[i])
            c.append(j[i])
            i += 1
        return c


if __name__ == '__main__':



    n = [4,2,5,7]
    p = Solution()
    a = p.sortArrayByParityII(n)
    print(a)



    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
