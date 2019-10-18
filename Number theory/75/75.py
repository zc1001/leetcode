import  math

#  python 可暴力
# 执行用时 :28 ms, 在所有 python 提交中击败了53.93% 的用户
# 内存消耗 :11.8 MB, 在所有 python 提交中击败了18.73%的用户
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        return nums

if __name__ == '__main__':



    n = [2,0,2,1,1,0]
    p = Solution()
    a = p.sortColors(n)
    print(a)



    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
