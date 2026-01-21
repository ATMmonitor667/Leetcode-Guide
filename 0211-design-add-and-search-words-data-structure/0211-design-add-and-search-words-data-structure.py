class TriNode(object):
    def __init__(self, char):
        self.currChar = char
        self.children = {}
        self.is_end = False

class WordDictionary(object):
    def __init__(self):
        self.root = TriNode('#')

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TriNode(char)
            node = node.children[char]
        node.is_end = True

    def dfs(self, word, i, node):
        # base case: consumed all characters
        if i == len(word):
            return node.is_end

        char = word[i]

        if char == '.':
            for ch, child in node.children.items():
                if self.dfs(word, i+1, child):
                    return True
            return False
        else:
            if char in node.children:
                return self.dfs(word, i+1, node.children[char])
            return False

    def search(self, word):
        return self.dfs(word, 0, self.root)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)