import  math

# 二分 python 可暴力
# 执行用时 :80 ms, 在所有 python 提交中击败了25.97% 的用户
# 内存消耗 :13.5 MB, 在所有 python 提交中击败了43.70%的用户
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #flage = True
        for i in matrix:
            if(target in i):
                return True
        return False
if __name__ == '__main__':



    n = [5, 7, 7, 8, 8, 10]
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    p = Solution()
    a = p.searchMatrix(matrix,7)
    print(a)

    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
