import  math

#  python
# 从最后一个数字开始循环 i表示从0到i之内的计算
#每次在范围之内找到最大的数字。判断，如果他在i的位置 跳过
#如果在0的位置， 在i 的位置翻转 存入i，进行一次翻转
#如果不在0和i的位置，存入最大值位置，i，进行一次最大值位置的翻转，一次i的翻转
#最后返回
# 执行用时 :36 ms, 在所有 python 提交中击败了67.50% 的用户
# 内存消耗 :11.8 MB, 在所有 python 提交中击败了9.09%的用户
class Solution(object):
    def nreverse(self, A, p):
        #print(reversed(A[:p]))
        A[:p+1] = reversed(A[:p+1])
        #print(A)

    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        length = len(A)-1
        c = []
        for i in range(len(A)-1,-1,-1):

            #print(i)
            if(A.index(max(A[0:length+1])) == length):
                length -= 1
                continue
            elif(A.index(max(A[0:length+1])) == 0):
                c.append(length+1)
                self.nreverse(A,length)
            else:
                c.append(A.index(max(A[0:length+1]))+1)
                c.append(length+1)
                self.nreverse(A,A.index(max(A[0:length+1])))
                self.nreverse(A,length)
            #print(A)
            length -= 1
        return c





if __name__ == '__main__':



    n = [2,1,3]
    #print(max(n[0:2]))
    p = Solution()
    a = p.pancakeSort(n)
    print(a)



    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
