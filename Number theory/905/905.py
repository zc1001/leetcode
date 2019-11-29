import  math
import  copy
import operator


# 执行用时 :72 ms, 在所有 python 提交中击败了71.14% 的用户
# 内存消耗 :12.2 MB, 在所有 python 提交中击败了35.72%的用户


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = []
        q = []
        for i in range(len(A)):
            if(A[i] % 2 == 0):
                q.append(A[i])
            if(A[i] %2 != 0):
                j.append(A[i])
        q += j
        return q



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
