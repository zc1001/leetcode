import  math

#  python 暴力
# 执行用时 :68 ms, 在所有 python 提交中击败了96.28% 的用户
# 内存消耗 :12.8 MB, 在所有 python 提交中击败了25.33%的用户
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))





if __name__ == '__main__':



    n = [2,1,3]
    #print(max(n[0:2]))
    p = Solution()
    a = p.pancakeSort(n)
    print(a)



    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
