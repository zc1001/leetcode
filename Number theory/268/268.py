# 执行用时 :128 ms, 在所有 python 提交中击败了90.38% 的用户
# 内存消耗 :12.5 MB, 在所有 python 提交中击败了30.72%的用户


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if(nums[i] != i):
                return i
        return nums[len(nums)-1] +1










if __name__ == '__main__':
    p = Solution()
    n1 = [1,2,3,0,0,0]
    n2 = [2,5,6]
    d = p.merge(n1,3,n2,3)
    print(d)

