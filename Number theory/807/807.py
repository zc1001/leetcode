import  math
import  copy
import operator


# 找行、列最大值
# 得到最小值
# 执行用时 :64 ms, 在所有 python 提交中击败了84.21% 的用户
# 内存消耗 :11.8 MB, 在所有 python 提交中击败了31.58%的用户


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = []
        l = []
        sum = 0
        for i in range(len(grid)):
            r.append(max(grid[i][:]))
        for i in range(len(grid[0])):
            g = []
            for j in range(len(grid)):
                g.append(grid[j][i])
            l.append(max(g))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                sum += min(r[i],l[j]) - grid[i][j]


        return sum












if __name__ == '__main__':





    n = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]


    #print(len(n))

    s = "anagram"
    t = "nagaram"
    #print(max(n[0:2]))
    p = Solution()

    # for i in range(1000000):
    #     j.append(p.monotoneIncreasingDigits(i))
    #     print(i)
    a = p.maxIncreaseKeepingSkyline(n)




    #a = p.charge(28)
    print(a)






    #p.compare(A,B)

    # [73, 74, 75, 71, 69, 72, 76, 73]

    #print(s)
    #print(test.lastSubstring("abab"))
