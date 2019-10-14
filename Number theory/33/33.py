import  math

# 直接return
#执行用时 :32 ms, 在所有 python 提交中击败了86.86% 的用户
#内存消耗 :11.9 MB, 在所有 python 提交中击败了20.12%的用户
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(target in nums):
            return nums.index(target)
        else:
            return -1
if __name__ == '__main__':



    n = [2,3,4]
    p = Solution()
    a = p.search(n,2)
    print(a)

    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
