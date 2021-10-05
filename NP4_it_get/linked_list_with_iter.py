from random import randint
from valid import check_int
from iterators import Iterator, generator
from nnode import Node


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
    
    def __str__(self):
        node = self.head
        s =''
        while node is not None:
            s += f"{node} "
            node = node.next
        return s


    def push_numbers(self, size, a=None, b=None):
        if a is not None and b is not None:
            obj = generator(size, a, b)
        else:
            obj = Iterator(size)
        node = Node(next(obj))
        self.head = node
        self.size += 1
        for i in obj:
            node.next = Node(i)
            node = node.next
            self.size += 1
        

    def put_into_tail(self, value):
        self.size += 1
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def pop_from_head(self):
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value


    def pop_from_tail(self):
        current_node = self.head
        for _ in range(self.size - 2):
            current_node = current_node.next
        value = current_node.value
        current_node.next = None
        self.size -= 1
        return value


    def put_into_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def insert(self, k, value):
        if k > self.size - 1:
            self.put_into_tail(value)
        elif k == 0:
            self.put_into_head(value)
        else:
            node = Node(value)
            current_node = self.head
            for _ in range(k-1):
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
            self.size += 1

    def pop(self, k):
        if k == 0:
            return self.pop_from_head()
        if k > self.size - 2:
            return self.pop_from_tail()
        current_node = self.head
        for _ in range(k-1):
            current_node = current_node.next
        value = current_node.next.value
        node = current_node.next.next
        current_node.next = node
        self.size -= 1
        return value    

    
    def left_shift(self, k):
        for _ in range(k):
            elem = self.pop(0)
            self.insert(self.size, elem) 