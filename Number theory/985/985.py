import  math
import  copy
import operator
from itertools import permutations
import numpy as np
import plotly as py
import plotly.graph_objs as go



# 执行用时 :516 ms, 在所有 python 提交中击败了84.96% 的用户
# 内存消耗 :17.9 MB, 在所有 python 提交中击败了8.90%的用户


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
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        l = []
        A[queries[0][1]] += queries[0][0]
        sum = 0
        for j in range(len(A)):
            if (A[j] % 2 == 0):
                sum += A[j]
        l.append(sum)
        if(len(A) == 1):
            return l
        for i in range(1,len(queries)):
            a = l[i-1]
            if(A[queries[i][1]] %2 == 0 ):
                a -= A[queries[i][1]]
                if((A[queries[i][1]] + queries[i][0])%2 == 0):
                    a += (A[queries[i][1]] + queries[i][0])
            else:
                if ((A[queries[i][1]] + queries[i][0]) % 2 == 0):
                    a += (A[queries[i][1]] + queries[i][0])
            A[queries[i][1]] += queries[i][0]
            l.append(a)
        return l




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


    a = p.canTransform("XXXLXXXXXX","XXXLXXXXXX")
    print(a)
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
