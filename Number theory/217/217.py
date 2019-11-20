# 执行用时 :124 ms, 在所有 python 提交中击败了72.41% 的用户
# 内存消耗 :15.7 MB, 在所有 python 提交中击败了39.67%的用户
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                return True
        return False










if __name__ == '__main__':
    p = Solution()
    n1 = [1,2,3,0,0,0]
    n2 = [2,5,6]
    d = p.merge(n1,3,n2,3)
    print(d)

