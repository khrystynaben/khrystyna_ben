import sys
from linked_list_with_iter import LinkedList
from valid import input_and_check
from random import uniform
from random import randint


def option(text, kk):
    for i in range (1, kk+1):
        print(f"Input {i} for",text[i])
    input_option = input_and_check( "? ", [str(x) for x in range(1,kk+1)])
    return input_option

def generations_limits():
    a = input_and_check("a = ", float)
    b = input_and_check("b = ", float)
    if a >= b:
        print("a must be less then b")
        sys.exit()
    return [a,b]

def generation(n_,li):
    arr_ab = generations_limits()
    a, b = arr_ab[0], arr_ab[1]
    li.push_numbers(n_, a, b)
    return li

def self_inputting(n, li):
    li.push_numbers(n)
    return li


def menu(li, n_):
    opt1 = option(['','creating list step by step', 'generating list randomly'],2)
    if opt1 =='1':
        array = self_inputting(n_, li)
    else:
        array = generation(n_,li)
    print(f"initial list: {li}")
    k = input_and_check("Input k: ", int, positive=True)
    opt2 = option(['','push on k position', 'delete from k position','shift k'],3)
    if opt2=='1':
        value = input_and_check("Input value: ", int)
        array.insert(k,value)
        print(array)
    elif opt2=='2':
        array.pop(3)
        print(array)
    else:
        array.left_shift(k)
        print(f"final list: {array}")


while True:
    ll = LinkedList()
    n = input_and_check("Input list quantity: ",int, positive=True)
    menu(ll,n)
    
    do_next = input_and_check("1 - next list; 2 - exit\n? ", ['1', '2'])
    if do_next == '2':
        break