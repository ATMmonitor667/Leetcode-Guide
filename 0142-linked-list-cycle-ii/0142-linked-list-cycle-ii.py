class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head

        # Step 1: detect if cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Step 2: find cycle entrance
        ptr1 = head
        ptr2 = slow

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1