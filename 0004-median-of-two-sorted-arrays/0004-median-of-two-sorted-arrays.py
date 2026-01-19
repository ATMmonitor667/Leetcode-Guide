class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()

        n = len(nums)

        if n % 2 == 1:
            return nums[n // 2]        
        else:
            mid1 = nums[n // 2 - 1]
            mid2 = nums[n // 2]
            return (mid1 + mid2) / 2.0
        