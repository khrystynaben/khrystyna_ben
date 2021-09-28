import sys
import datetime as dt

def show_error(text):
    print(text)
    sys.exit()

def wrong(x):
    print(f'Wrong {x}!')
    sys.exit()


def is_integer(x):
    return isinstance(x, int)

def is_positive(x):
    return is_number(x) and x >= 0

def is_positive_integer(x): 
    return is_integer(x) and is_positive(x)

 
def change_to_integer(x): 
    try:
        temp_var = int(x)
    except:
        show_error('must be integer')
    return temp_var

def change_to_float(x): 
    try:
        temp_var = float(x)
    except:
        show_error('must be float')
    return temp_var


def is_number(x): 
    return isinstance(x, (int, float))

def is_value(x, values): 
    return x in values

def valid_specific_elem(x,l):
    if is_value(x,l)==True:
        return x
    else:
        show_error('incorrect value')

def valid_int_posit(x):
    if is_positive_integer(x):
        return x

def dt_valid(date_):
    try:
        dtm = dt.datetime.strptime(date_, '%Y/%m/%d')
    except:
        wrong(f'{date_}')
    return dtm
