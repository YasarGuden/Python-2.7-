class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2
node2.next = node3

