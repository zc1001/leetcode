import  math
import  copy
import operator


# 执行用时 :136 ms, 在所有 python 提交中击败了92.76% 的用户
# 内存消耗 :18 MB, 在所有 python 提交中击败了100.00%的用户


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        return nums



if __name__ == '__main__':
    twitter = Twitter()
    #print(twitter.user)
    twitter.postTweet(1, 5)
    #print(twitter.user)
    twitter.getNewsFeed(1)
    #print(twitter.user)
    twitter.follow(1, 2)
    #print(twitter.user)
    twitter.postTweet(2, 6)
    #print(twitter.user)
    twitter.getNewsFeed(1)
    twitter.unfollow(1, 2)
    twitter.getNewsFeed(1)






    n = [0,2,3,4,6,8,9]
    b = [0,2,3,4,6,8,9]


    #print(len(n))

    s = "anagram"
    t = "nagaram"
    #print(max(n[0:2]))
    #p = Solution()

    # for i in range(1000000):
    #     j.append(p.monotoneIncreasingDigits(i))
    #     print(i)
    #a = p.summaryRanges(n)




    #a = p.charge(28)
    #print(a)






    #p.compare(A,B)

    # [73, 74, 75, 71, 69, 72, 76, 73]

    #print(s)
    #print(test.lastSubstring("abab"))
