class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
  
        """
        hold = letters[0]
        maxNum = float('inf')

        for i in letters:
            if ord(i) > ord(target):
                diff = ord(i) - ord(target)

                if diff < maxNum:
                    maxNum = diff
                    hold = i

        return hold

        