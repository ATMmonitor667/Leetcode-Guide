class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        abcabcbb -> for this problem, window which increases whenever a previous is not encountered
        [a,c,d] ...  the moment a duplicate word does show up we are going to shrink the
        wordWindow down until the window is unique again. So im thinking a while condition
        is broken inside the forloop ofcourse,
        standard template for solving sliding window problems is as the following
        def function slidingWindow():
              left = 0
              window ={} or []
              for right in range(len(nums)):
                window.append(nums[right]) | -> slided to the right or the wdindow you can
                say is ever growing
                Then we have a while loopwhere the fucntion shrinks, or thewindow shrinks
                maxLength = max(maxLength, right - left + 1)
        """
        left = 0
        window = []
        maxLength = 0
        for right in range(len(s)):
            while s[right] in window and left < len(s):
                window.remove(s[left])
                left = left + 1
            window.append(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength