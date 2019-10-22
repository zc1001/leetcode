import  math

#python 直接return
# 执行用时 :44 ms, 在所有 python 提交中击败了77.36% 的用户
# 内存消耗 :13.3 MB, 在所有 python 提交中击败了10.93%的用户
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2 = list(s)
        t2 = list(t)
        s2.sort()
        t2.sort()
        if(s2 == t2):
            return True
        else:
            return False




if __name__ == '__main__':



    n = [-1,0,3,5,9,12]
    s = "anagram"
    t = "nagaram"
    #print(max(n[0:2]))
    p = Solution()
    a = p.isAnagram(s,t)
    print(a)



    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
