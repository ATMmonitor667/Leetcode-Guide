# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        two arrays which linkedlist values
        reverse the arrays 
        while i incrementally decrease
        and where i of both lists dont equal each other we break from the loop
        so the previous hold value is the first value in the array where both are equal
        return the holdvalue
        """
        if not headA or not headB:
            return None

        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
        