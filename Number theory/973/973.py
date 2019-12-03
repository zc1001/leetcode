import  math
import  copy
import operator


# 用字典，key距离，value索引
# 执行用时 :752 ms, 在所有 python 提交中击败了58.46% 的用户
# 内存消耗 :19.2 MB, 在所有 python 提交中击败了5.60%的用户


import string



class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        l = {}
        for i in range(len(points)):
            a =math.sqrt((points[i][0]**2 + points[i][1]**2))
            if a in l:
                l[a].append(i)
            else:
                l[a] = []
                l[a].append(i)
        l2 =  sorted(l.items(), key = lambda k: k[0])
        i = K
        j = 0
        p = []
        for k,v in l2:
            t = len(v)-1
            while(i>0 and t>=0):
                p.append(points[v[t]])
                i-=1
                t-=1
            if(i<0):
                break
        return p




if __name__ == '__main__':













    n = [[1,3],[-2,2]]
    b = [0,2,3,4,6,8,9]


    #print(len(n))

    s = "anagram"
    t = "nagaram"
    #print(max(n[0:2]))
    p = Solution()

    # for i in range(1000000):
    #     j.append(p.monotoneIncreasingDigits(i))
    #     print(i)
    a = p.kClosest(n,1)
    print(a)




    #a = p.charge(28)
    #print(a)






    #p.compare(A,B)

    # [73, 74, 75, 71, 69, 72, 76, 73]

    #print(s)
    #print(test.lastSubstring("abab"))
