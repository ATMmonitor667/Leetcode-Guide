class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.res = [-1]*n
        self.ptr = 0
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.res[idKey-1] = value
        if self.res[self.ptr] == -1:
            return []
        ans = []
        while self.ptr < len(self.res) and self.res[self.ptr] != -1 :
            ans.append(self.res[self.ptr])
            self.ptr+=1
        return ans 
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)