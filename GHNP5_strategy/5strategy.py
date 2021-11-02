from abc import abstractmethod
from iterators import Iterator
from linked_list_with_iter import LinkedList


class Strategy():

    @abstractmethod
    def pushing_numbers(self):
        pass


class ConcreteStrategyA(Strategy):

    def __init__(self, ll:LinkedList, pos, n, a, b):
        self.ll = ll
        self.pos = pos
        self.n = n
        self.a = a
        self.b = b

    def pushing_numbers(self):
        list_ = LinkedList()
        list_.push_random_numbers(self.n, self.a, self.b)
        self.ll.inserting_on_position(self.pos, list_)
        return self.ll


class ConcreteStrategyB(Strategy):

    def __init__(self, ll:LinkedList, pos, file_name):
        self.ll = ll
        self.pos = pos
        self.file_name = file_name

    def pushing_numbers(self):
        list_= LinkedList()
        list_.push_numbers_from_file(self.file_name)
        self.ll.inserting_on_position(self.pos, list_)
        return self.ll
        
