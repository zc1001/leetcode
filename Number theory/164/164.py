import  math
import  copy
import operator
from itertools import permutations
import numpy as np
import plotly as py
import plotly.graph_objs as go


# 执行用时 :68 ms, 在所有 python 提交中击败了27.15% 的用户
# 内存消耗 :12.3 MB, 在所有 python 提交中击败了36.84%的用户


import string
import os

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

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

# class Solution(object):
#     def cha(self,a):
#         for i in range(len(a)):
#             a[i] = abs(a[i] - 1)
#         return a
#     def matrixScore(self, A):
#         """
#         :type A: List[List[int]]
#         :rtype: int
#         """
#         R, C = len(A), len(A[0])
#         ans = 0
#         for c in range(C):
#             col = 0
#             for r in range(R):
#                 col += A[r][c] ^ A[r][0]
#             ans += max(col, R - col) * 2 ** (C - 1 - c)
#         return ans


def nthPersonGetsNthSeat( n):
    """
    :type n: int
    :rtype: float
    """
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(n>1):
        return 0.5
def point_plots():
    N = 1000  # 设置1000个散点，这个可以自由变化
    random_x = np.random.randn(N)  # 调用Np包中的正态分布函数，生成N个点
    random_y = np.random.randn(N)
    # 也可以用其他随机函数生成，详细可以看起它包的随机函数
    # Create a trace#plotly包中常用trace变量来表示轨迹
    trace0 = go.Scatter(
        x=random_x,
        y=random_y,
        mode='markers'  # 散点图
    )
    data = [trace0]

    py.offline.plot(data, filename='basic-scatter.html')  # 生成一个basic-scatter的html文件
    print('OK')  # 表示运行结束的信息
def line_plots():
    trace1 = go.Scatter(
        x=[1, 2, 3, 4, 5,
           6, 7, 8, 9, 10,
           11, 12, 13, 14, 15],
        y=[10, 20, None, 15, 10,
           5, 15, None, 20, 10,
           10, 15, 25, 20, 10],
        name='<b>No</b> Gaps',  # Style name/legend entry with html tags
        connectgaps=True
    )
    trace2 = go.Scatter(
        x=[1, 2, 3, 4, 5,
           6, 7, 8, 9, 10,
           11, 12, 13, 14, 15],
        y=[5, 15, None, 10, 5,
           0, 10, None, 15, 5,
           5, 10, 20, 15, 5],
        name='Gaps',
        connectgaps=True
    )

    data = [trace1, trace2]

    fig = dict(data=data)
    py.offline.plot(fig, filename='simple-connectgaps.html')


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<2):
            return 0
        nums.sort()
        n = 0
        for i in range(len(nums)-1):
            if((nums[i+1] - nums[i])>n ):
                n = nums[i+1] -nums[i]
        return n



if __name__ == '__main__':
    # iris = datasets.load_iris()
    # data = iris.data
    # target = iris.target
    # dat1 = np.array(data)
    # label = np.array(target)
    # np.savetxt('D:\DataFusion\DataFusion\网络数据集\iris\data.txt', dat1, fmt='%0.3f')
    # np.savetxt('D:\DataFusion\DataFusion\网络数据集\iris\label.txt',label,fmt='%0.0f')


    #A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    # B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    # customers = [1, 0, 1, 2, 1, 1, 7, 5]
    # grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    # st = "abbaca"
    p = Solution()


    a = p.numPairsDivisibleBy60([14,161,302,232,270,428,155,64,499,400,25,349,434,427,5,265,20,346,463,10,1,163,189,345,390,212,498,281,308,482,447,217,318,239,374,449,298,213,2,230,5,500,300,390,139,484,464,477,111,88,93,198,181,113,393,283,383,205,42,292,335,392,384,268,361,462,413,176,118,111,143,242,166,286,177,52,126,342,415,302,210,48,369,148,209,87,212,53,296,95,97,45,467,47,373,404,43,439,19,64,289,218,268,460,238,456,490,155,429,218,301,225,228,237,453,267,259,327,427,169,176,322,216,451,29,327,404,177,225,44,248,174,287,326,441,354,110,4,226,324,331,158,454,469,354,383,336,211,133,500,233,330,471,327,426,478,195,232,163,312,126,51,161,248,433,348,464,206,480,478,98,354,304,424,338,382,431,379,194,488,6,494,394,469,430,1,207,307,172,47,269,472,415,163,309,68,213,175,343,187,15,232,429,389,373,143,146,88,58,320,116,82,482,125,343,329,115,116,183,389,112,294,74,89,62])
    #print(a)
    # #
    #
    #
    #
    # for i in range(100):
    #     print(i,p.bulbSwitch(i))
    # a = np.random.uniform(-math.pi,math.pi)
    # print(a)
    # l = []
    # x = []
    # for i in range(-200,200):
    #     l.append(1/np.tanh(x))
    #     x.append(i)
    # plt.plot(x,l)
    # plt.show()
    #line_plots()

    # print(a)
    # import numpy as np
    # from sklearn import datasets
    # from sklearn.model_selection import train_test_split
    # from sklearn.model_selection import GridSearchCV
    # from sklearn.preprocessing import StandardScaler
    # from sklearn.neighbors import KNeighborsClassifier
    #
    # # 加载 sklearn 中的 datasets 数据中的digits（手写字体数据）
    #
    # digits = datasets.load_digits()
    # x = digits.data
    # y = digits.target
    #
    # # 使用 train_test_split 进行模型建立和测试的分离,加zhiqian是因为没有进行
    # # 归一化处理
    #
    # X_train_zhiqian, X_test_zhiqian, y_train, y_test = train_test_split(x, y, test_size=0.2)
    #
    # # 使用 StandardScaler进行归一化处理
    # """为什么使用X_train_zhiqian进行归一化处理的均值和方差进行对X_test的归一化呢？
    # 是因为要服从现实情况，如果只有一个数据进行预测，就没有办法得出均值和方差
    # """
    #
    # s = StandardScaler()
    # s.fit(X_train_zhiqian)
    # X_train = s.transform(X_train_zhiqian)
    # X_test = s.transform(X_test_zhiqian)
    #
    # knn_clf = KNeighborsClassifier()
    # # 使用网格搜索的方法进行对超参数的选取
    # # 超参数是指在算法进行时对不确定的参数进行调整以使得算法的预测准确率最高
    # params = [
    #     {"weights": ["uniform"],
    #      "n_neighbors": [k for k in range(1, 11)]
    #      },
    #     {"weights": ["distance"],
    #      "n_neighbors": [k for k in range(1, 11)],
    #      "p": [k for k in range(1, 6)]
    #      }
    # ]
    #
    # # n_jobs 这个参数是使用计算机的几个核，赋值为-1表示全都使用
    #
    # gridsearch = GridSearchCV(knn_clf, params, n_jobs=-1)
    # gridsearch.fit(X_train, y_train)
    # print("best_score", gridsearch.best_score_)
    # print("best_params", gridsearch.best_params_)
    #
    # # 将最好的赋值给knn_clf
    # knn_clf = gridsearch.best_estimator_
    #
    # print(knn_clf.score(X_test, y_test))
