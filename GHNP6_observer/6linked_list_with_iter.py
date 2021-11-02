from iterators import Iterator
from nnode import Node
from os.path import exists
import sys


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
    
    def get_size(self):
        return self.size

    def __str__(self):
        node = self.head
        s =''
        while node is not None:
            s += f"{node} "
            node = node.next
        return s


    def push_numbers_from_file(self, file_name): 
        if exists(file_name): 
            with open(file_name, 'r') as f: 
                for line in f : 
                    row = line.split() 
                    n = len(row)
                    node = Node(int(row[0]))
                    self.head = node
                    self.size += 1
                    for j in range(1,n):
                        node.next = Node(int(row[j]))
                        node = node.next
                        self.size += 1                                
        else: 
            sys.exit(f'{file_name} does not exists')


    def push_random_numbers(self, size, a=None, b=None):
        obj = Iterator(size,a,b)
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

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def length(self):
        k = 0
        for _ in self:
            k += 1
        return k

    def inserting_on_position(self, pos, list_):
        if self.length() != 0 or pos < self.length():
            for i,elem in enumerate(list_):
                self.insert(pos+i, elem)
        else:
            for i in list_:
                self.put_into_tail(i)

    def pop_elements(self, start, end):
        if ((start and end) >0) and end>start and ((start and end) <self.length()):
            for i in range(start, end+1):
                self.pop(i)
        else:
            print('incorrect positions')