import  math
import  copy
import operator


# 用字典
# 执行用时 :144 ms, 在所有 python 提交中击败了32.62% 的用户
# 内存消耗 :15.1 MB, 在所有 python 提交中击败了36.36%的用户


import string



class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort()
        l = {}
        k2 = 1
        #print(nums)
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                k2 += 1
            else:
                if k2 in l:
                    l[k2].append(nums[i])
                    k2 = 1
                else:
                    l[k2] = []
                    l[k2].append(nums[i])
                    k2 = 1
        if(k2>=1):
            if k2 in l:
                l[k2].append(nums[len(nums)-1])
            else:
                l[k2] = []
                l[k2].append(nums[len(nums)-1])
                k2 = 1
        e = sorted(l.items(),key=lambda item:item[0],reverse=True)
        i = k
        #print(e)
        o = []
        for K,V in e:
            x = len(V)-1
            while(i>0 and x>=0):
                o.append(V[x])
                x -= 1
                i -= 1
        return o








if __name__ == '__main__':













    n = [4,1,-1,2,-1,2,3]
    b = [0,2,3,4,6,8,9]


    #print(len(n))

    s = "anagram"
    t = "nagaram"
    #print(max(n[0:2]))
    p = Solution()

    # for i in range(1000000):
    #     j.append(p.monotoneIncreasingDigits(i))
    #     print(i)
    a = p.topKFrequent(n,2)
    print(a)




    #a = p.charge(28)
    #print(a)






    #p.compare(A,B)

    # [73, 74, 75, 71, 69, 72, 76, 73]

    #print(s)
    #print(test.lastSubstring("abab"))
