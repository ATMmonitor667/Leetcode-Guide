# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def add(l1,l2):
            dummy = ListNode(0)
            cursor = dummy
            carry = 0

            while l1 or l2 or carry:
                x = l1.val if l1 else 0
                y = l2.val if l2 else 0

                s = x + y + carry
                carry = s // 10
                digit = s % 10

                cursor.next = ListNode(digit)
                cursor = cursor.next

                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None

            return dummy.next
        def reverseList(head):
            prev = None
            current = head
                
            while current:
                nextPtr = current.next    
                current.next = prev       
                prev = current            
                current = nextPtr         
                
            return prev
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        l3 = add(l1,l2)
        l3 = reverseList(l3)
        return l3


        