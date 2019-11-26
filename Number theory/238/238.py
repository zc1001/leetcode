import  math
import  copy
import operator


# 执行用时 :100 ms, 在所有 python 提交中击败了96.19% 的用户
# 内存消耗 :21 MB, 在所有 python 提交中击败了6.03%的用户


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        r = [0]*len(nums)
        s = []
        sum = 1
        for i in range(len(nums)):
            sum *= nums[i]
            l.append(sum)
        sum = 1
        for i in range(len(nums)-1,-1,-1):
            sum *= nums[i]
            r[i] = sum
        s.append(r[1])
        for i in range(1,len(nums)-1):
            s.append(l[i-1]*r[i+1])
        s.append(l[len(nums)-2])
        return s










if __name__ == '__main__':





    n = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    b = [1,2,3,4]


    #print(len(n))

    s = "anagram"
    t = "nagaram"
    #print(max(n[0:2]))
    p = Solution()

    # for i in range(1000000):
    #     j.append(p.monotoneIncreasingDigits(i))
    #     print(i)
    a = p.productExceptSelf(b)




    #a = p.charge(28)
    print(a)






    #p.compare(A,B)

    # [73, 74, 75, 71, 69, 72, 76, 73]

    #print(s)
    #print(test.lastSubstring("abab"))
