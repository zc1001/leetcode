import  math

# 直接return
# 执行用时 :84 ms, 在所有 python 提交中击败了89.34% 的用户
# 内存消耗 :13.6 MB, 在所有 python 提交中击败了5.32%的用户
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        list = []
        if(target in nums):
            for i in range(len(nums)):
                if(nums[i] == target):
                    list.append(i)
            return [list[0],list[len(list)-1]]
        else:
            return -1
if __name__ == '__main__':



    n = [5, 7, 7, 8, 8, 10]
    p = Solution()
    a = p.searchRange(n,6)
    print(a)

    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
