"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return head

        def compress(node):
            cur = node
            tail = node

            while cur:
                nxt = cur.next

                if cur.child:
                    child_head = cur.child
                    cur.child = None

                    cur.next = child_head
                    child_head.prev = cur

                    child_tail = compress(child_head)

                    child_tail.next = nxt
                    if nxt:
                        nxt.prev = child_tail

                    tail = child_tail
                    cur = child_tail
                else:
                    tail = cur

                cur = cur.next

            return tail

        compress(head)
        return head



        