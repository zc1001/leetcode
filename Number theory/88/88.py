# 执行用时 :32 ms, 在所有 python 提交中击败了46.60% 的用户
# 内存消耗 :11.7 MB, 在所有 python 提交中击败了28.17%的用户
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num = nums1[:m]
        #print(num)
        for i in range(n):
            num.append(nums2[i])
        for i in range(len(nums1)-m-n):
            num.append(0)
        num.sort()
        return num







if __name__ == '__main__':
    p = Solution()
    n1 = [1,2,3,0,0,0]
    n2 = [2,5,6]
    d = p.merge(n1,3,n2,3)
    print(d)

