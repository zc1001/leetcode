# 复杂度没有达到要求 但还是过了
# 执行用时 :336 ms, 在所有 Python 提交中击败了97.61%的用户
# 内存消耗 :19.1 MB, 在所有 Python 提交中击败了47.53%的用户


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        q = []
        p = [0]*(len(nums)+1)
        for i in range(len(nums)):
            p[nums[i]] +=1
        for i in range(1,len(p)):
            if(p[i] == 0):
                q.append(i)
        return q









if __name__ == '__main__':
    p = Solution()
    n1 = [1,2,3,0,0,0]
    n2 = [2,5,6]
    d = p.merge(n1,3,n2,3)
    print(d)

