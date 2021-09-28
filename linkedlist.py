from random import randint
from valid import check_int

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def push_from_keyboard(self, size):
        elem = check_int(input(f'Input element 1: '))
        node = Node(elem)
        self.head = node
        self.size += 1
        for i in range(size-1):
            elem = check_int(input(f'Input element {i+2}: '))
            node.next = Node(elem)
            node = node.next
            self.size += 1

    def push_randomly(self, size, a, b):
        elem = randint(a, b)
        node = Node(elem)
        self.head = node
        self.size += 1
        for i in range(size-1):
            elem = randint(a, b)
            node.next = Node(elem)
            node = node.next
            self.size += 1
        
    def __str__(self):
        node = self.head
        s =''
        while node is not None:
            s += f"{node} "
            node = node.next
        return s

    def append(self, value):
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
            self.append(value)
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
        elif k > self.size - 2:
            self.pop_from_tail()
        else:
            current_node = self.head
            for _ in range(k-1):
                current_node = current_node.next
            value = current_node.next.value
            node = current_node.next.next
            current_node.next = node
            self.size -= 1
            return value    