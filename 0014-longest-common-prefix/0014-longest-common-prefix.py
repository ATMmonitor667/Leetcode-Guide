class TrieNode:
    def __init__(self):
        
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    def prefixFind(self, word):
        node = self.root
        prefix = ''
        for ch in word:
            if ch not in node.children:
                return prefix
            prefix+=ch
            node = node.children[ch]
        return prefix





class Solution(object):
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        hold = Trie()
        hold.add_word(strs[0])
        globalPrefix = strs[0]

        for i in range(1,len(strs)):
            currPrefix = hold.prefixFind(strs[i])
            if currPrefix == '':
                return ''
            if len(currPrefix) > len(globalPrefix):
                continue
            else:
                globalPrefix = currPrefix
        return globalPrefix

        