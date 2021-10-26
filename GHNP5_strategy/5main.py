import sys
from linked_list_with_iter import LinkedList
from valid import file_check, input_and_check
from context import Context


def print_all_options():
    print('\n''   Input 1 for choose 1st strategy''\n'
        '   Input 2 for choose 2nd strategy''\n'
        '   Input 3 for generate list with chosen strategy''\n'
        '   Input 4 for delete element from position''\n'
        '   Input 5 for delete elements''\n'
        '   Input 6 for use left_shift''\n'
        '   Input 7 for print list''\n'
        '   Input 8 for end work''\n')

def generations_limits():
    a = input_and_check("a = ", float)
    b = input_and_check("b = ", float)
    if a >= b:
        print("a must be less then b")
        sys.exit()
    return [a,b]


def menu(li, cont):
    while True:
        print_all_options()
        opt1 = input_and_check('Choose the option: ', [str(x) for x in range(1,9)])
        if opt1 =='1':
            cont.set_strategy(1)
            print('You chose the first strategy')
        elif opt1 == '2':
            cont.set_strategy(2)
            print('You chose the second strategy')
        elif opt1 == '3':
            position = input_and_check("Input the position: ",int, positive=True)
            if cont.get_strategy == 1:
                n = input_and_check("Input n: ", int, positive=True)
                ab = generations_limits()
                a = ab[0]
                b = ab[1]
                li = cont.push_numbers(li, position, n, a, b)
            else:
                file_name = input('Input file name: ')
                file_name = file_check(file_name)
                li = cont.push_numbers(li,position,file_name)
            print('generated list:',li)
        elif opt1 == '4':
            position_to_delete = input_and_check("Input the position to delete: ",int, positive=True)
            li.pop(position_to_delete)
        elif opt1 == '5':
            start_pos = input_and_check('input the position from which you want to delete: ', int, positive=True)
            end_pos = input_and_check('input the position t0 which you want to delete: ', int, positive=True)
            li.pop_elements(start_pos,end_pos)
        elif opt1 == '6':
            k = input_and_check("Input k: ", int, positive=True)
            li.left_shift(k)
        elif opt1 == '7':
            print(f"initial list: {li}")
        elif opt1 == '8':
            break


  
    


ll = LinkedList()
cont = Context()
menu(ll, cont)
    