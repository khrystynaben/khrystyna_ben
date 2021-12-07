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

 ##########################################


def validate_int_and_posit(x):
    if isinstance(x, str):
        x = change_to_integer(x)
    if is_positive_integer(x):
        return x
    wrong(f'{x}')

def validate_specific_str(x, sym, list_, number_of_parts, index_spec_part):
    if x is None:
        return f'no_{x}'
    temp_var = str(x)
    parts = temp_var.split(sym)
    if len(parts) != number_of_parts or parts[index_spec_part] not in list_:
        wrong(f'{x}')
    return temp_var

def validate_float_and_posit(x): 
    if isinstance(x, str):
        x = change_to_float(x)
    if x >= 0:
        return x
    wrong('amount')

def validate_specific_elem(x, list_):
    if is_value(x, list_)==True:
        return x
    else:
        wrong(f'{x}')

def validate_date(x):
    if isinstance(x,str):
        try:
            return dt.datetime.strptime(x, '%Y-%m-%d')  
        except:
            wrong(f'{x}')
    return x

def validate_second_date(x, y):
    c = validate_date(x)
    d = validate_date(y)
    if d>=c:
        return d
    else:
        wrong(f'{y} have to be bigger')


def validate_str_with_digits(x, sym, numb_of_parts): 
    parts = str(x).split(sym)
    if len(parts)==numb_of_parts and len(parts[0])==8 and len(parts[1].strip())==2 and parts[0].isdigit() and parts[1].strip().isdigit():
        return x
    wrong(f'{x}')


def validate_int(x):
    if isinstance(x, str):
        x = change_to_integer(x)
        return x
    wrong(f'{x}')