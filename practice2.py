from random import uniform
from random import randint
import sys

operations = 0


def show_error(text):
    print(text)
    sys.exit()


def type_change(x, type_x):
    try:
        temp_var = type_x(x)
    except:
        show_error(f"must be {str(type_x).split(chr(39))[-2]}")
    return temp_var


def full_checking(x, type_check, positive=False):
    if type_check is int:
        temp_var = type_change(x, int)
        if positive == True and temp_var < 0:
            show_error('must be positive')
        return temp_var
    elif type(type_check) is list:
        if x not in type_check:
            show_error('incorrect option')
        return x
    elif type_check is float:
         return type_change(x, float)


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
    operations += 4
    while True:
        operations += 1
        if list_1[i] < list_2[j]:
            merged.append(list_1[i])
            i += 1
            operations += 2
            if i == len(list_1):
                merged.extend(list_2[j:])
                operations += 1
                break
        else:
            merged.append(list_2[j])
            j += 1
            operations += 2
            if j == len(list_2):
                merged.extend(list_1[i:])
                operations += 1
                break
    for i in range(len(list_)):
        list_[i] = merged[i]
        operations += 1
    return list_


def input_and_check(text, type_check, positive=False):
    temp_var = input(text)
    temp_var = full_checking(temp_var, type_check, positive=False)
    return temp_var


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


def generation(n_):
    arr_ab = generations_limits()
    a, b = arr_ab[0], arr_ab[1]
    type_option = option(['','choosing integer', 'choosing float'],2)
    if type_option == '1':
        array_ = [randint(a, b) for _ in range(n_)]
    else:
        array_ = [uniform(a, b) for _ in range(n_)]
    return array_


def self_inputting():
    array_ = []
    for i in range(n):
        element = input_and_check(f"Input element {i + 1}: ", float)
        array_.append(element)
    return array_


def general_inputting(n_):
    type_option = option(['','creating list step by step', 'generating list randomly'], 2)
    if type_option == '1':
        array = self_inputting()
    else:
        array = generation(n_)
    return array


while True:
    n = input_and_check('n = ', int, positive=True)
    array = general_inputting(n)
    print(f"Initial list: {array}")
    merge_sort(array)
    print(f"After sorting: {array}")
    print("Number of operations: ", operations)
    do_next = input_and_check("1 - next list; 2 - exit\n? ", ['1', '2'])
    if do_next == '2':
        break
