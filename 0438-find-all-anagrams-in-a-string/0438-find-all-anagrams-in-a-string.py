class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        k = len(p)
        if len(s) < k:
            return []

        pmap = Counter(s[:k])   
        smap = Counter(p)      
        res = []

        for i in range(len(s) - k + 1):
            if pmap == smap:
                res.append(i)

            if i + k < len(s):  
                left = s[i]
                right = s[i + k]

                pmap[left] -= 1
                if pmap[left] == 0:
                    del pmap[left]   

                pmap[right] += 1

        return res

