import  math

#  python 可暴力
# 执行用时 :72 ms, 在所有 python 提交中击败了23.80% 的用户
# 内存消耗 :11.7 MB, 在所有 python 提交中击败了33.59%的用户
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c = []
        if(len(nums1)>len(nums2)):
            long = nums1
            short = nums2
        else:
            long = nums2
            short = nums1
        for i in range(len(short)):
            if(short[i] in long):
                c.append(short[i])
                long.remove(short[i])
        return c


if __name__ == '__main__':



    n = [3,1,3,4,2]
    p = Solution()
    a = p.findDuplicate(n)
    print(a)



    #p.compare(A,B)





    #print(s)
    #print(test.lastSubstring("abab"))
