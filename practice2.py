from random import uniform
from random import randint
import sys

operations = 0

def integer_checking(x):
    try:
        temp_var = int(x)
    except:
        print('must be integer')
        sys.exit()
    return temp_var


def full_checking(x, type_check):
    if type_check == 'int and posit':
        temp_var = integer_checking(x)
        if temp_var <= 0:
            print('must be positive')
            sys.exit()
        return temp_var
    elif type_check == '1/2':
        temp_var = integer_checking(x)
        if (temp_var == 1 or temp_var == 2) == False:
            print('must be 1 or 2')
            sys.exit()
        return temp_var
    else:
        try:
            temp_var = float(x)
        except:
            print('must be number')
            sys.exit()
        return temp_var


def merge_sort(list_):
    global operations
    size = len(list_)
    operations += 1
    if size < 2:
        operations += 1
        return list_[:]
    list_1 = merge_sort(list_[:size//2])
    list_2 = merge_sort(list_[size//2:])
    i = j = 0
    merged = []
    operations += 5
    while True:
        operations += 1
        if list_1[i] < list_2[j]:
            merged.append(list_1[i])
            i += 1
            operations += 3
            if i == len(list_1):
                merged.extend(list_2[j:])
                operations += 1
                break
        else:
            merged.append(list_2[j])
            j += 1
            operations += 3
            if j == len(list_2):
                merged.extend(list_1[i:])
                operations += 1
                break
    for i in range(len(list_)):
        list_[i] = merged[i]
        operations += 1
    return list_


while True:
    n = input("n = ")
    n = full_checking(n, 'int and posit')
    print("Input 1 for creating list step by step")
    print("Input 2 for generate list automatically")
    input_option = input("? ")
    input_option = full_checking(input_option, '1/2')
    if input_option == 1:
        array = []
        for i in range(n):
            element = input(f"Input element {i + 1}: ")
            element = full_checking(element, 'other')
            array.append(element)
    else:
        a = input("a = ")
        a = full_checking(a, 'other')
        b = input("b = ")
        b = full_checking(b, 'other')
        print("Input 1 if you choose integer ")
        print("Input 2 if you choose for float")
        type_option = input('? ')
        type_option = full_checking(type_option, '1/2')
        if type_option == 1:
            array = [randint(a, b) for _ in range(n)]
        else:
            array = [uniform(a, b) for _ in range(n)]
    print(f"Initial list: {array}")
    merge_sort(array)
    print(f"After sorting: {array}")
    print("Number of operations: ", operations)
    do_next = input("1 - next list; 2 - exit\n? ")
    do_next = full_checking(do_next, '1/2')
    if do_next == 2:
        break