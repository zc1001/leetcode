import  math

#  python 可暴力
# 执行用时 :64 ms, 在所有 python 提交中击败了88.33% 的用户
# 内存消耗 :13.5 MB, 在所有 python 提交中击败了34.71%的用户
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1,len(nums)):
            if(nums[i] == nums[i-1]):
                return nums[i]
        return 0

if __name__ == '__main__':



    n = [3,1,3,4,2]
    p = Solution()
    a = p.findDuplicate(n)
    print(a)



    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
