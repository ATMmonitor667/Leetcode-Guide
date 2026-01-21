class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class MagicDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary):
        for w in dictionary:
            node = self.root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end = True

    def search(self, searchWord):
        def dfs(node, i, usedEdit):
            if i == len(searchWord):
                return usedEdit and node.end

            ch = searchWord[i]

            if ch in node.children:
                if dfs(node.children[ch], i + 1, usedEdit):
                    return True

            if not usedEdit:
                for nxt_ch, nxt_node in node.children.items():
                    if nxt_ch == ch:
                        continue
                    if dfs(nxt_node, i + 1, True):
                        return True

            return False

        return dfs(self.root, 0, False)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)