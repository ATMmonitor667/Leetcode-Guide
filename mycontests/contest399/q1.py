class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        the way to solve this problem is the find the number of pairs in a linear order
        first we can implement the O(n^2) solution and then move on to the
        linear time order solution.
        """
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]%(nums2[j]*k)==0 and nums2[j]!=0:
                    count +=1
        return count