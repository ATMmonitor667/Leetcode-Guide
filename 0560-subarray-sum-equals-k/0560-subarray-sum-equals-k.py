class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        prefix[r]-prefix[l-1] = k
        [0,1,1,1] = [3]-[1]=2
                    [2]-[0]=2
        [0,1,2,3] = [1+2]-[0]
                  = [3]-0
        [0,1,3,6]  [3-0]=3, [6-3]=3
        prefix[l-1] = prefix[r]-k
        freq(prefix[l-1])+=1
        count += freq(prefix[r]-k)
        freq = {0:1} = prefix Sum of zero occured 1
        1
        freq = {0:1, 1:1} so prefixSum of 1 occured once
        freq = {0:1, 1:1 3:1} so the prefixSum of 3 occured once, k = 3, how manytimes
        has 3-3 happened? that happened once
        freq = {0:1, 1:1, 3:1, 6:1} prefixSum of 6 has happened 1 once,
        how many times has k=3 6-3 = 3(this is the k) 6 (right) 3(left) = 3(looking for)
        6 - 3 = 3 
        +=1


        """
        count = 0
        curr = 0
        seen = {0:1}
        for i in nums:
            curr += i
            if curr -k in seen:
                count += seen[curr - k]
            seen[curr] = seen.get(curr, 0) + 1
        return count 