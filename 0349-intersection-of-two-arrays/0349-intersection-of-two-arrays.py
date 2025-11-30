class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        A = set(nums1)
        B = set(nums2)
        C = A.intersection(B)
        ans = list(C)
        return ans