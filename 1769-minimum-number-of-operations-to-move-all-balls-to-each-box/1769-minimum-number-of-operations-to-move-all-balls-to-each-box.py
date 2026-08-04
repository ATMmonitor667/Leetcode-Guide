class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        hashmap[1] = (indexs)
        for i in range(len(boxes)):
            ans.append(sum([abs(i-val) for key,val in hashmap.items()])
        """
        arr = []
        for index, value in enumerate(boxes):
            if value == '1':
                arr.append(index)
        ans = []
        for i in range(len(boxes)):
            ans.append(sum([abs(i-val) for val in arr]))
        print(ans)
        return ans 