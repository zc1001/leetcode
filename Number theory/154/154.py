import  math

# 二分 python 可暴力
# 执行用时 :36 ms, 在所有 python 提交中击败了98.94% 的用户
# 内存消耗 :12 MB, 在所有 python 提交中击败了33.00%的用户
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
