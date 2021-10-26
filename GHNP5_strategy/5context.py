from strategy import *


class Context():

    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy
    
    @property
    def get_strategy(self):
        return self.strategy

    def push_numbers(self, *args):
        if self.strategy == 1:
            s = ConcreteStrategyA(*args)
        else:
            s = ConcreteStrategyB(*args)
        return s.pushing_numbers()

