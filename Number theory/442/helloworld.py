# 时间复杂度没有达到要求 但还是过了
# 执行用时 :612 ms, 在所有 Python 提交中击败了5.13%的用户
# 内存消耗 :18.8 MB, 在所有 Python 提交中击败了31.52%的用户


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                l.append(nums[i])
        return sum










if __name__ == '__main__':
    p = Solution()
    n1 = [1,2,3,0,0,0]
    n2 = [2,5,6]
    d = p.merge(n1,3,n2,3)
    print(d)

