import  math
import  copy
import operator


# 直接算
# 执行用时 :96 ms, 在所有 python 提交中击败了16.91% 的用户
# 内存消耗 :11.7 MB, 在所有 python 提交中击败了38.71%的用户

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        d = []
        a = []
        for i in range(len(S)):
            if(S[i] == C):
                d.append(i)
        for i in range(len(S)):
            min = 1000
            min_num = 0
            for j in range(len(d)):
                if(min > abs(d[j] - i )):
                    min = abs(d[j] - i )
                    min_num = d[j]
            a.append(d[min_num])
        return a









if __name__ == '__main__':





    n2 = [2]


    #print(len(n))

    s = "anagram"
    t = "nagaram"
    #print(max(n[0:2]))
    p = Solution()

    # for i in range(1000000):
    #     j.append(p.monotoneIncreasingDigits(i))
    #     print(i)
    a = p.findMedianSortedArrays(n,n2)




    #a = p.charge(28)
    print(a)






    #p.compare(A,B)

    # [73, 74, 75, 71, 69, 72, 76, 73]

    #print(s)
    #print(test.lastSubstring("abab"))
