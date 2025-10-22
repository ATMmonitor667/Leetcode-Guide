class Solution(object):
    def minSplitMerge(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        dfs(l,r,target)
        """
        if nums1 == nums2:
            return 0

        start = tuple(nums1)
        target = tuple(nums2)
        q = deque([(start, 0)])
        seen = {start}

        while q:
            arr, count = q.popleft()
            n = len(arr)

            for left in range(n):
                for right in range(left, n):
                    segment = arr[left:right+1]
                    rest = arr[:left] + arr[right+1:]
                    
                    # insert the segment anywhere in rest
                    for pos in range(len(rest) + 1):
                        # skip re-inserting at the original place
                        if pos == left:
                            continue
                        new_arr = rest[:pos] + segment + rest[pos:]
                        if new_arr == target:
                            return count + 1
                        if new_arr not in seen:
                            seen.add(new_arr)
                            q.append((new_arr, count + 1))
        return -1
            
        