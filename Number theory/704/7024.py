import  math

# 执行用时 :248 ms, 在所有 python 提交中击败了96.42% 的用户
# 内存消耗 :12.8 MB, 在所有 python 提交中击败了17.77%的用户
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            return -1





if __name__ == '__main__':



    n = [-1,0,3,5,9,12]
    #print(max(n[0:2]))
    p = Solution()
    a = p.search(n,2)
    print(a)



    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
