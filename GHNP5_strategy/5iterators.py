from valid import check_int
from random import randint


def generator(n, a, b):
    for i in range(n):
        yield randint(a, b)


class Iterator:
    def __init__(self, n,a,b):
        self.n = n
        self.a = a
        self.b = b
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.n:
            self.counter += 1
            return randint(self.a,self.b)
        else:
            raise StopIteration