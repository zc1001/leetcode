import  math
import  copy
import operator


# 执行用时 :24 ms, 在所有 python 提交中击败了40.21% 的用户
# 内存消耗 :11.7 MB, 在所有 python 提交中击败了32.43%的用户


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if(len(nums) == 0):
            return []
        result_str = ""
        result_str += str(nums[0])
        i = 0
        result = []
        while(i<len(nums)-1):
            if((nums[i]+1) == nums[i+1] or nums[i] == nums[i+1]):
                i += 1
                continue
            else:
                if(int(result_str) == nums[i]):
                    result.append(result_str)
                    result_str = str(nums[i+1])
                else:
                    result_str += '->'
                    result_str += str(nums[i])
                    result.append(result_str)
                    result_str = str(nums[i+1])
                i += 1
        if (int(result_str) == nums[len(nums)-1]):
            result.append(result_str)
        else:
            result_str += '->'
            result_str += str(nums[len(nums)-1])
            result.append(result_str)

        return result



if __name__ == '__main__':





    n = [0,2,3,4,6,8,9]
    b = [0,2,3,4,6,8,9]


    #print(len(n))

    s = "anagram"
    t = "nagaram"
    #print(max(n[0:2]))
    p = Solution()

    # for i in range(1000000):
    #     j.append(p.monotoneIncreasingDigits(i))
    #     print(i)
    a = p.summaryRanges(n)




    #a = p.charge(28)
    print(a)






    #p.compare(A,B)

    # [73, 74, 75, 71, 69, 72, 76, 73]

    #print(s)
    #print(test.lastSubstring("abab"))
