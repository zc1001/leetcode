# 执行用时 :24 ms, 在所有 python 提交中击败了42.27% 的用户
# 内存消耗 :11.8 MB, 在所有 python 提交中击败了18.42%的用户
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.d = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.d.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        a = d[self.count]
        self.count += 1
        #self.d.pop()
        return a

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """

        return self.d[self.count]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if(len(self.d)-1 < self.count):
            return True
        else:
            return False










if __name__ == '__main__':
    p = Solution()
    n1 = [1,2,3,0,0,0]
    n2 = [2,5,6]
    d = p.merge(n1,3,n2,3)
    print(d)

