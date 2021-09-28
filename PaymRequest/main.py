from os.path import exists
from valid import valid_specific_elem
from pr import PaymentRequest
from collect import Collection
import sys

c = Collection('dani.txt')
print(c)

while True:
    c.menu(c)
    do_next = input("1 - next; 2 - exit\n? ")
    do_next = valid_specific_elem(do_next, ['1', '2'])
    if do_next == '2':
        break


