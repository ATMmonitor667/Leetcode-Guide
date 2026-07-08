class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        count = Counter(arr)
        seen = set()
        for key,v in count.items():
            if v == 1:
                seen.add(key)
        
        for i in range(len(arr)):
            if arr[i] in seen:
                k-=1
            if k == 0:
                return arr[i]
        return ""
            
        