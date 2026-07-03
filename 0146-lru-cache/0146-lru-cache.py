class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.currSize = 0

        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        """
        Remove node from linked list.
        """
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insert_front(self, node):
        """
        Insert node right after head.
        This makes it the most recently used.
        """
        firstNode = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = firstNode
        firstNode.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert_front(node)

        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.remove(node)
            self.insert_front(node)

        else:
            if self.currSize == self.size:
                lastNode = self.tail.prev

                self.remove(lastNode)
                del self.cache[lastNode.key]

                self.currSize -= 1

            node = Node(key, value)
            self.cache[key] = node
            self.insert_front(node)
            self.currSize += 1



                


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)