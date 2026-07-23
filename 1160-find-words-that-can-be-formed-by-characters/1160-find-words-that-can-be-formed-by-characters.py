class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        charMap = Counter(chars)
        count = 0 
        for word in words:
            wordMap = Counter(word)
            print(wordMap)
            flag = True
            for key, value in wordMap.items():
                if key not in charMap or value > charMap[key]:
                    flag = False
                    break
            if flag:
                count+=len(word)
        return count
            