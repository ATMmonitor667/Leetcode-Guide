class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3)%2==1:
            return nums3[len(nums3)//2]
        else:
            mid = len(nums3)//2
            another = mid-1
            summation = float(nums3[mid]+nums3[another])/2
            return summation 
        