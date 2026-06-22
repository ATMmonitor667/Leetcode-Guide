# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        arr = []
        cursor = head

        while cursor:
            arr.append(cursor.val)
            cursor = cursor.next

        hold = float('-inf')

        for i in range(len(arr) // 2):
            currSum = arr[i] + arr[len(arr) - 1 - i]
            if currSum > hold:
                hold = currSum

        return hold
