# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        MergeSort application on this linkedlist
        """
    def sortList(self, head):
        def merge(l1, l2):
            dummy = ListNode(0)
            cur = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next

            # attach remainder (CRUCIAL)
            cur.next = l1 if l1 else l2
            return dummy.next

        def get_length(node):
            n = 0
            while node:
                n += 1
                node = node.next
            return n

        def split_by_length(node):
           
            n = get_length(node)
            if n <= 1:
                return node, None

            mid = n // 2 
            prev = None
            cur = node

            for _ in range(mid):
                prev = cur
                cur = cur.next

            prev.next = None

            left = node
            right = cur
            return left, right

        def sort(node):
            if not node or not node.next:
                return node

            left, right = split_by_length(node)
            left = sort(left)
            right = sort(right)
            return merge(left, right)

        return sort(head)
        
            
          