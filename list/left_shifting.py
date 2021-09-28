import sys
import linked_list
from valid import check_int, check_in, check_order

def left_shift(ll, k):
    for _ in range(k):
        elem = ll.pop(0)
        ll.insert(ll.size, elem) 

ll = linked_list.LinkedList()
n = check_int(input("Input list quantity: "), positive=True)
print("Input 1 for creating list step by step; Input 2 for generate list automatically")
option = check_in(input('? '), ['1', '2'])
if option == '1':
    ll.push_from_keyboard(n)
else:
    a = check_int(input('a = '))
    b = check_int(input('b = '))
    check_order(a, b)
    ll.push_randomly(n, a, b)
print(f"initial list: {ll}")
k = check_int(input("Input k: "), positive=True)
left_shift(ll, k)
print(f"final list: {ll}")