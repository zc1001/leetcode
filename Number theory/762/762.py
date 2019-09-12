import  math
# python 直接暴力
# 用两个内置函数 bin 转二进制 打表计算是不是质数 主要还是计算最后能出现的最大质数
# 执行用时 :1548 ms, 在所有 Python 提交中击败了5.51% 的用户
# 内存消耗 :12.1 MB, 在所有 Python 提交中击败了9.30%的用户
# 特别菜
class Solution(object):
    def Dec2Bin(self,dec):
        result = ''
        if dec:
            result = self.Dec2Bin(dec // 2)
            return result + str(dec % 2)
        else:
            return result

    def is_prime(self, x):
        arr = [0,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]
        if(arr[x] == 1):
            return True
        else:
            return False

    def countPrimeSetBits(self, L, R):
        sum = 0
        for i in range(L,R+1):
            s = bin(i)
            num = 0
            for i in s:
                if(i == "1"):
                    #print("hhhhhh")
                    num += 1
            if(self.is_prime(num)):
                sum += 1
        return sum








if __name__ == '__main__':
    p = Solution()
    print(p.countPrimeSetBits(10,15))





    #print(s)
    #print(test.lastSubstring("abab"))
