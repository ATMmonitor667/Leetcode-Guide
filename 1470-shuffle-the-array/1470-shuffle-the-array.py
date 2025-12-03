class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arr1 = nums[0:n]
        arr2 = nums[n:]
        arr3 = []
        i = 0
        j = 0
        k = 0
        while i < n and j < n:
            if k%2 == 0:
                arr3.append(arr1[i])
                i+=1
                k+=1
            if k%2 == 1:
                arr3.append(arr2[j])
                j+=1
                k+=1
        return arr3

        