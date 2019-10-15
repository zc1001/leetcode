import  math

# 二分 python 可暴力
# 执行用时 :36 ms, 在所有 python 提交中击败了91.82% 的用户
# 内存消耗 :11.9 MB, 在所有 python 提交中击败了21.14%的用户
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums2 = nums[:]
        nums2.sort()
        #print(nums2)
        #print(nums)
        #print(nums.index(nums2[len(nums2)-1]))
        return nums.index(nums2[len(nums2)-1])
        #return 0


if __name__ == '__main__':



    n = [1,2,3,1]
    p = Solution()
    a = p.findPeakElement(n)
    print(a)



    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
