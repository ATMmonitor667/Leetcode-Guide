class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
      
        lookup = Counter(nums)
        print(lookup)
        ans = []
        for i in range(len(nums)):
            if nums[i] == 0:
                ans.append(0)
            else:
                key = nums[i]-1
                count = 0
                while key != -1:
                    if key in lookup:
                        count += lookup[key]
                    key-=1
                ans.append(count)
        return ans 

       


        