import  math

# 二分 python 可暴力
# 执行用时 :24 ms, 在所有 python 提交中击败了98.75% 的用户
# 内存消耗 :12.1 MB, 在所有 python 提交中击败了5.33%的用户
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[0]
if __name__ == '__main__':



    n = [3,4,5,1,2]
    p = Solution()
    a = p.findMin(n)
    print(a)



    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
