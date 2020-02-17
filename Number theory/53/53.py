# 直接遍历不合要求
# 执行用时 :336 ms, 在所有 Python 提交中击败了97.61%的用户
# 内存消耗 :19.1 MB, 在所有 Python 提交中击败了47.53
# 执行用时 :168 ms, 在所有 Python 提交中击败了18.18% 的用户
# 内存消耗 :12.8 MB, 在所有 Python 提交中击败了100.00%的用户


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if(nums[i] != i):
                return i
        return(nums[len(nums)-1]+1)








if __name__ == '__main__':
    print('j')

