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
        arr1 = []
        arr2 = []

        while l1:
            arr1.append(l1.val)
            l1 = l1.next
        while l2:
            arr2.append(l2.val)
            l2 = l2.next

        arr1 = arr1[::-1]
        arr2 = arr2[::-1]

        i = 0
        carry = 0
        ans = []

        while (i < len(arr1) and i < len(arr2)) or carry:
            val1 = arr1[i] if i < len(arr1) else 0
            val2 = arr2[i] if i < len(arr2) else 0

            total = val1 + val2 + carry
            ans.append(total % 10)
            carry = total // 10
            i += 1

        while i < len(arr1):
            total = arr1[i] + carry
            ans.append(total % 10)
            carry = total // 10
            i += 1

        while i < len(arr2):
            total = arr2[i] + carry
            ans.append(total % 10)
            carry = total // 10
            i += 1

        ans = ans[::-1]

        dummy = ListNode(0)
        currNode = dummy

        for val in ans:
            currNode.next = ListNode(val)
            currNode = currNode.next

        return dummy.next

        