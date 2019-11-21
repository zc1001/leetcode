# 执行用时 :36 ms, 在所有 python 提交中击败了91.14% 的用户
# 内存消耗 :12.7 MB, 在所有 python 提交中击败了31.71%的用户
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        t = []
        for i in range(len(nums)):
            if(nums[i] != 0):
                #print(nums[i])
                t.append(nums[i])
        for i in range(len(nums)):
            if(nums[i] == 0):
                #print(nums[i])
                t.append(0)
        for i in range(len(nums)):
            nums[i] = t[i]










if __name__ == '__main__':
    p = Solution()
    n1 = [1,2,3,0,0,0]
    n2 = [2,5,6]
    d = p.merge(n1,3,n2,3)
    print(d)

