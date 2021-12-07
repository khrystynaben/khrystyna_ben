from caretaker import CareTaker
from collect import Collection
from valid import *
from menu import *


c = Collection('js.json')
print(c)

n = input_and_check('number of states: ', int, positive=True)
handler = CareTaker(c, n)

while True:
    menu(c, handler)
    do_next = input("1 - next; 2 - exit\n? ")
    do_next = validate_specific_elem(do_next, ['1', '2'])
    if do_next == '2':
        break


