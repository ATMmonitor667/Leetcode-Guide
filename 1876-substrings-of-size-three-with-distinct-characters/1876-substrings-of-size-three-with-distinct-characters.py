class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        we have a window which tracks the 3 letters
        every slide the window first removes the left most 
        and before adding the right most checks if that char is in the
        window, if yes do nothing if no add one to the count,
        return the count at the end. Why does this work hashmap allows there
        to be 
        """
        count = 0
        for i in range(len(s) - 2):
            a = s[i]
            b = s[i+1]
            c = s[i+2]
            if a != b and a != c and b != c:
                count += 1
                
        return count
        