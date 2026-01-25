# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        
        length = 0
        cursor = head
        while cursor:
            length += 1
            cursor = cursor.next
        length -= n
        cursor = dummy
        while length > 0:
            length -= 1
            cursor = cursor.next
            
        cursor.next = cursor.next.next
        
        return dummy.next