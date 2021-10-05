import sys


def show_error(text):
    print(text)
    sys.exit()


def check_int(x, positive=False):
    try:
        int_number = int(x)
    except:
        sys.exit('must be integer')
    if positive and int_number <= 0:
        sys.exit('must be positive')
    return int_number


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


def input_and_check(text, type_check, positive=False):
    temp_var = input(text)
    temp_var = full_checking(temp_var, type_check, positive=False)
    return temp_var