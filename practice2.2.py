from random import uniform
from random import randint
import sys

operations = 0


def show_error(text):
    print(text)
    sys.exit()


def try_check(x, type_x):
    try:
        temp_var = type_x(x)
    except:
        show_error(f"must be {str(type_x).split(chr(39))[-2]}")
    return temp_var


def full_checking(x, type_check, positive=False):
    if type_check is int:
        temp_var = try_check(x, int)
        if positive == True and temp_var < 0:
            show_error('must be positive')
        return temp_var
    elif type(type_check) is list:
        if x not in type_check:
            show_error('incorrect option')
        return x
    elif type_check is float:
         return try_check(x, float)


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


def generation(n_):
    a = input("a = ")
    a = full_checking(a, float)
    b = input("b = ")
    b = full_checking(b, float)
    if a >= b:
        print("a must be less then b")
        sys.exit()
    print("Input 1 if you choose integer ")
    print("Input 2 if you choose for float")
    type_option = input('? ')
    type_option = full_checking(type_option, ['1','2'])
    if type_option == '1':
        array_ = [randint(a, b) for _ in range(n_)]
    else:
        array_ = [uniform(a, b) for _ in range(n_)]
    return array_


def self_inputting():
    array_ = []
    for i in range(n):
        element = input(f"Input element {i + 1}: ")
        element = full_checking(element, float)
        array_.append(element)
    return array_


def inputting(n_):
    print("Input 1 for creating list step by step")
    print("Input 2 for generate list automatically")
    input_option = input("? ")
    input_option = full_checking(input_option, ['1', '2'])
    if input_option == '1':
        array = self_inputting()
    else:
        array = generation(n_)
    return array


while True:
    n = input("n = ")
    n = full_checking(n, int, positive=True)
    array = inputting(n)
    print(f"Initial list: {array}")
    merge_sort(array)
    print(f"After sorting: {array}")
    print("Number of operations: ", operations)
    do_next = input("1 - next list; 2 - exit\n? ")
    do_next = full_checking(do_next, ['1', '2'])
    if do_next == '2':
        break