import sys

def check_int(x, positive=False):
    try:
        int_number = int(x)
    except:
        sys.exit('must be integer')
    if positive and int_number <= 0:
        sys.exit('must be positive')
    return int_number

def check_in(x, values):
    if x not in values:
        sys.exit(f"bad option")
    return x

def check_order(x, y):
    if x >= y:
        sys.exit(f"incorrect value")