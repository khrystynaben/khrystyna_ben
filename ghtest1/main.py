from collection import Collection
from menu import *

c = Collection('dani.txt')
print(c)

while True:
    menu(c)
    do_next = input("1 - next; 2 - exit\n? ")
    do_next = validate_specific_elem(do_next, ['1', '2'])
    if do_next == '2':
        break