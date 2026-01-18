# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        li3 = ListNode(0)
        cursor = li3
        while list1 and list2:
            if list1.val <= list2.val:
                cursor.next = ListNode(list1.val)
                cursor = cursor.next
                list1 = list1.next
            elif list1.val > list2.val:
                cursor.next = ListNode(list2.val)
                cursor = cursor.next
                list2 = list2.next
        if list1:
            cursor.next = list1
        else:
            cursor.next = list2
        return li3.next
            

