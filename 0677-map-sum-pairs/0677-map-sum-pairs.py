class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cursor = self.root
        for c in word:
            if c not in cursor.children:
                cursor.children[c] = TrieNode()
            cursor = cursor.children[c]
        cursor.is_end = True

    def findPrefix(self, word):
        cursor = self.root
        for c in word:
            if c not in cursor.children:
                return False
            cursor = cursor.children[c]
        return True

class MapSum(object):

    def __init__(self):
        self.mp = {}
        self.root = Trie()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.root.addWord(key)
        if key not in self.mp:
            self.mp[key] = val
        else:
            self.mp[key] =val
    
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0
        for key, val in self.mp.items():
            if key.startswith(prefix):
                total += val
        return total

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)