class Node:
    """An object for storing a single node of a linked list.
    Models two attribute - data and the link to the next node in the list"""

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" %self.data

N1 = Node(10)
print(N1)

N2 = Node(20)
N1.next_node = N2
print(N1.next_node)

class LinkedList:
    """Singlely Linked List"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """Return the number of nodes in the last.
        Takes O(n) time"""

        current = self.head
        count = 0 

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """Adds new node containing data at head of the list
        Takes O(1) time"""

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def __repr__(self):
        """Return a string representation of the list
        Takes O(n)time"""

        nodes = []
        current = self.head

        while current: 
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.size()
print(l)

print(l.size())

