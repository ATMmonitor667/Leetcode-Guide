class MyHashMap(object):

    def __init__(self):
        self.mapp = {}
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.mapp:
            self.mapp[key] = value
        self.mapp[key] = value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.mapp:
            return -1
        return self.mapp[key]
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.mapp:
            return -1
        del self.mapp[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)