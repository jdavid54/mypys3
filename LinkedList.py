import numpy as np

# item : node[value, child-item]

# linkedList : [head-item,             tail-item,        list length]

# empty list : [ None,                 None,                 0]
# one item   : [ [value1, node1],      [value1, None],       1]      node1 = [value1, None]
# 2 items    : [ [value1, node1],      [value2, node2],      2]      node1 = [value1, node2], node2 = [value2, None]
# 3 items    : [ [value1, node1],      [value3, node3],      3]      node1 = [value1, node2], node2 = [value2, node3], node3 = [value3, None]

class Item():
    def __init__(self, value):
        self.value = value
        self.child = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        node = Item(value)
        if self.head == None:
            self.head = node
            self.head.child = node
            self.tail = node
        else:
            self.tail.child = node
            self.tail = node
        self.length += 1

    def insertAfter(self, target, value):
        node = Item(value)
        pointer = self.head
        while pointer != None and pointer.value != target:
            pointer = pointer.child
        if pointer != None:   # target node
            node.child = pointer.child      # get next node to target and copy to node child
            pointer.child = node            # target child = node
        else:   # last node
            print(self.tail.value)
            self.tail.child = node
            self.tail = node
        self.length += 1
    
    def shift(self):    # delete first node
        if self.head == None:
            return None
        node = self.head
        self.head = node.child
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return node
    
    def __str__(self):
        if self.head == None:
            return "Empty"
        cur = self.head
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.child
        out += "EOLL"  # end-of-linked-list
        return out

values = [1,2,3,4,"end"]
linkedList = LinkedList()

for value in values:
    linkedList.push(value)
    
print(linkedList)
# insert item
linkedList.insertAfter(8,6)   # insert at the end of list because 8 does not exist
print(linkedList)

linkedList.insertAfter(3,6)
print(linkedList)
for num in range(linkedList.length):
    print(linkedList.shift().value)
    
print("Length:", linkedList.length)
print("Done")