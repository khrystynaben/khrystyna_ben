from valid import check_int
from random import randint


def generator(n, a, b):
    for i in range(n):
        yield randint(a, b)


class Iterator:
    def __init__(self, n):
        self.n = n
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.n:
            self.counter += 1
            return check_int(input(f'Input element {self.counter}: '))
        else:
            raise StopIteration