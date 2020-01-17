import numpy
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

# 执行用时 :28 ms, 在所有 Python 提交中击败了47.52% 的用户
# 内存消耗 :11.8 MB, 在所有 Python 提交中击败了27.66%的用户

# def download_data( file_path):
#     # 下载对应的数据，
#     # 返回训练数据、训练标签、测试数据、测试标签
#
#     # 训练数据的数据、标签
#     train_data = []
#     train_label = []
#     # 测试数据的数据、标签
#     test_data = []
#     test_label = []
#     file_path = '/home/zc1001/FeatureExtraction/不同浓度的气体传感器阵列漂移数据集/data'
#     # 读取数据
#     filepath_traindata = file_path + '/train/data.txt'
#     filepath_trainlabel = file_path + '/train/label.txt'
#     filepath_testdata = file_path + '/test/data.txt'
#     filepath_testlabel = file_path + '/test/label.txt'
#     # 下载训练数据
#     train_data = numpy.loadtxt(filepath_traindata, dtype=numpy.float32)
#     train_label = numpy.loadtxt(filepath_trainlabel, dtype=numpy.float32)
#     # 下载测试数据
#     test_data = numpy.loadtxt(filepath_testdata, dtype=numpy.float32)
#     test_label = numpy.loadtxt(filepath_testlabel, dtype=numpy.float32)
#     # 返回训练数据、测试数据
#     return train_data, train_label, test_data, test_label
# if __name__ == '__main__':
#     data_train,label_train,data_test,label_test = download_data('a')
#     max_mean = 0  # 最大训练精度
#     best_k = 1  # 最好的K值
#     for i in range(1, 30):
#         knn = KNeighborsClassifier(i)
#         scores = cross_val_score(knn, data_train, label_train, cv=10, scoring='accuracy')
#         if (scores.mean() > max_mean):
#             # 找到更大精度的K值
#             best_k = i
#             max_mean = scores.mean()
#     # 已找到最好的k
#
#     # 再次进行训练，保存模型
#     knn = KNeighborsClassifier(n_neighbors=best_k)  # 模型创建
#     knn.fit(data_train, label_train)  # 开始训练
#     KNNModel = knn
#     y_test = KNNModel.predict(data_test)
#     correct_num = sum(y_test == label_test)
#     # 计算准确度
#     accuracyRate = numpy.mean(y_test == label_test)
#     print(correct_num)
#     print(accuracyRate)
#     a = [1.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,1.0,1.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,1.0,0.0,1.0,1.0,1.0,1.0,0.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,1.0,1.0,1.0,1.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,1.0,1.0]
#     sum = 0
#     for i in range(len(a)):
#         if(a[i] == 1):
#             sum += 1
#     print(sum)
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1 = []
        t1 = []
        for i in range(len(s)):
            s1.append(s[i])
        for i in range(len(t)):
            t1.append(t[i])
        s1.sort()
        t1.sort()

        for i in range(len(s)):
            if(s1[i] == t1[i]):
                continue
            else:
                return t1[i]
        return t1[len(t1)-1]
if __name__ == '__main__':
    so = Solution()

    s = "ymbgaraibkfmvocpizdydugvalagaivdbfsfbepeyccqfepzvtpyxtbadkhmwmoswrcxnargtlswqemafandgkmydtimuzvjwxvlfwlhvkrgcsithaqlcvrihrwqkpjdhgfgreqoxzfvhjzojhghfwbvpfzectwwhexthbsndovxejsntmjihchaotbgcysfdaojkjldprwyrnischrgmtvjcorypvopfmegizfkvudubnejzfqffvgdoxohuinkyygbdzmshvyqyhsozwvlhevfepdvafgkqpkmcsikfyxczcovrmwqxxbnhfzcjjcpgzjjfateajnnvlbwhyppdleahgaypxidkpwmfqwqyofwdqgxhjaxvyrzupfwesmxbjszolgwqvfiozofncbohduqgiswuiyddmwlwubetyaummenkdfptjczxemryuotrrymrfdxtrebpbjtpnuhsbnovhectpjhfhahbqrfbyxggobsweefcwxpqsspyssrmdhuelkkvyjxswjwofngpwfxvknkjviiavorwyfzlnktmfwxkvwkrwdcxjfzikdyswsuxegmhtnxjraqrdchaauazfhtklxsksbhwgjphgbasfnlwqwukprgvihntsyymdrfovaszjywuqygpvjtvlsvvqbvzsmgweiayhlubnbsitvfxawhfmfiatxvqrcwjshvovxknnxnyyfexqycrlyksderlqarqhkxyaqwlwoqcribumrqjtelhwdvaiysgjlvksrfvjlcaiwrirtkkxbwgicyhvakxgdjwnwmubkiazdjkfmotglclqndqjxethoutvjchjbkoasnnfbgrnycucfpeovruguzumgmgddqwjgdvaujhyqsqtoexmnfuluaqbxoofvotvfoiexbnprrxptchmlctzgqtkivsilwgwgvpidpvasurraqfkcmxhdapjrlrnkbklwkrvoaziznlpor"
    t = "qhxepbshlrhoecdaodgpousbzfcqjxulatciapuftffahhlmxbufgjuxstfjvljybfxnenlacmjqoymvamphpxnolwijwcecgwbcjhgdybfffwoygikvoecdggplfohemfypxfsvdrseyhmvkoovxhdvoavsqqbrsqrkqhbtmgwaurgisloqjixfwfvwtszcxwktkwesaxsmhsvlitegrlzkvfqoiiwxbzskzoewbkxtphapavbyvhzvgrrfriddnsrftfowhdanvhjvurhljmpxvpddxmzfgwwpkjrfgqptrmumoemhfpojnxzwlrxkcafvbhlwrapubhveattfifsmiounhqusvhywnxhwrgamgnesxmzliyzisqrwvkiyderyotxhwspqrrkeczjysfujvovsfcfouykcqyjoobfdgnlswfzjmyucaxuaslzwfnetekymrwbvponiaojdqnbmboldvvitamntwnyaeppjaohwkrisrlrgwcjqqgxeqerjrbapfzurcwxhcwzugcgnirkkrxdthtbmdqgvqxilllrsbwjhwqszrjtzyetwubdrlyakzxcveufvhqugyawvkivwonvmrgnchkzdysngqdibhkyboyftxcvvjoggecjsajbuqkjjxfvynrjsnvtfvgpgveycxidhhfauvjovmnbqgoxsafknluyimkczykwdgvqwlvvgdmufxdypwnajkncoynqticfetcdafvtqszuwfmrdggifokwmkgzuxnhncmnsstffqpqbplypapctctfhqpihavligbrutxmmygiyaklqtakdidvnvrjfteazeqmbgklrgrorudayokxptswwkcircwuhcavhdparjfkjypkyxhbgwxbkvpvrtzjaetahmxevmkhdfyidhrdeejapfbafwmdqjqszwnwzgclitdhlnkaiyldwkwwzvhyorgbysyjbxsspnjdewjxbhpsvj"

    c = so.findTheDifference(s,t)
    print(c)