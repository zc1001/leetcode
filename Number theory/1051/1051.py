import  math
import  copy
import operator


# 执行用时 :24 ms, 在所有 python 提交中击败了74.11% 的用户
# 内存消耗 :11.9 MB, 在所有 python 提交中击败了100.00%的用户


import string
import os
import numpy as np
import matplotlib.pyplot as plt
# def get_filelist(strl):
#     l = []
#     s1 = strl
#     for i in range(8):
#         s = s1
#         l.append(s + '\通道'+str(i)+'.txt')
#     return l
# def mkdir(path):
#     # 引入模块
#     import os
#
#     # 去除首位空格
#     path = path.strip()
#     # 去除尾部 \ 符号
#     path = path.rstrip("\\")
#
#     # 判断路径是否存在
#     # 存在     True
#     # 不存在   False
#     isExists = os.path.exists(path)
#
#     # 判断结果
#     if not isExists:
#         # 如果不存在则创建目录
#         # 创建目录操作函数
#         os.makedirs(path)
#         return True
#     else:
#         # 如果目录存在则不创建，并提示目录已存在
#         return False
#
# def read_file(filename):
#     channel = []
#     for i in range(len(filename)):
#         with open(filename[i], 'r') as file_to_read:
#             a = []
#             while True:
#                 lines = file_to_read.readline()  # 整行读取数据
#                 if not lines:
#                     break
#                 list = lines.split()
#                 a.append(float(list[1]))
#         channel.append(a)
#     return channel
# def shift(channel):
#     sum = 0
#     b = 2000
#     for i in range(b):
#         sum += channel[4][i]
#     averange = sum/b
#
#     # sum1 = 0
#     # for i in range(b):
#     #     sum1 += channel[1][i]
#     # averange1 = sum1/b
#     # heigh = averange-averange1
#     # for i in range(len(channel[1])):
#     #     channel[1][i] += heigh
#     #
#     # sum1 = 0
#     # for i in range(b):
#     #     sum1 += channel[5][i]
#     # averange1 = sum1 / b
#     # heigh = averange - averange1
#     # for i in range(len(channel[5])):
#     #     channel[5][i] += heigh
#     #
#     # sum1 = 0
#     # for i in range(b):
#     #     sum1 += channel[6][i]
#     # averange1 = sum1 / b
#     # heigh = averange - averange1
#     # for i in range(len(channel[6])):
#     #     channel[6][i] += heigh
#     #
#     # sum1 = 0
#     # for i in range(b):
#     #     sum1 += channel[7][i]
#     # averange1 = sum1 / b
#     # heigh = averange - averange1
#     # for i in range(len(channel[7])):
#     #     channel[7][i] += heigh
#     for j in range(len(channel[0])):
#         channel[0][j] -= averange
#     for i in range(2,5):
#         for j in range(len(channel[i])):
#             channel[i][j] -= averange
#
#
#     return channel
#
#
# def write_file(l,filepath):
#     for i in range(len(l)):
#         if (len(l[i]) == 0):
#             continue
#         else:
#             mkdir(filepath)  # 创建文件夹
#             filename = filepath + '\\' + '通道' + str(i) + '.txt'
#             with open(filename, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
#                 for j in range(len(l[i])):
#                     str_file = str(round(j * 0.4, 1)) + ' ' + str(l[i][j])
#                     f.write(str_file + "\n")

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        l = heights[:]
        heights.sort()
        sum = 0
        for i in range(len(heights)):
            if(l[i] != heights[i]):
               sum += 1
        return sum


if __name__ == '__main__':
    # filepath = "F:\shuju\output\put\d"
    # put_filepath = "F:\shuju\output\put\dnew"
    # l = get_filelist(filepath)
    # ln = []
    # channel = read_file(l)
    # channel_new  = shift(channel)
    # write_file(channel_new,put_filepath)
    # fig = plt.figure()
    # for i in range(8):
    #     plt.plot(channel_new[i],label=str(i))
    #
    #    # plt.ylabel("纵轴： "+str(i), fontproperties='simhei', fontsize=20)
    # #plt.legend(handles=ln, labels=['1','2','3','4','5','6','7','8'])
    # #plt.grid(alpha=0.4,linestyle=':')
    # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0,
    #            ncol=3, mode="expand", borderaxespad=0.)
    # plt.annotate("Important value", (55, 20), xycoords='data',
    #              xytext=(5, 38),
    #              arrowprops=dict(arrowstyle='->'))
    # plt.show()
    #print('a')















    #n = [4,1,-1,2,-1,2,3]
    # b = [0,2,3,4,6,8,9]
    #
    #
    # #print(len(n))
    #
    # s = "anagram"
    # t = "nagaram"
    # #print(max(n[0:2]))
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    st = "abbaca"
    p = Solution()
    #
    # # for i in range(1000000):
    # #     j.append(p.monotoneIncreasingDigits(i))
    # #     print(i)
    a = p.removeDuplicates(st)
    print(a)




    #a = p.charge(28)
    #print(a)






    #p.compare(A,B)

    # [73, 74, 75, 71, 69, 72, 76, 73]

    #print(s)
    #print(test.lastSubstring("abab"))
