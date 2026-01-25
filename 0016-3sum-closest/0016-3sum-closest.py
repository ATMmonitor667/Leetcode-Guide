class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        # Initialize with the sum of the first three numbers
        currAns = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if abs(target - current_sum) < abs(target - currAns):
                    currAns = current_sum
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                else:
                    
                    return current_sum
                    
        return currAns
            
        