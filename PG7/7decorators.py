import datetime as dt
from valid import*
from my_exceptions import ValidationError
import re
from functools import wraps


def validation_int(func):
    @wraps(func)
    def wrapper(*args):
        if isinstance(args[1], str):
            if args[1][0] != '0' and args[1][1:].isdigit() and (args[1][0].isdigit() or args[1][0] == '-' ):
                return func(args[0],int(args[1]))
            else:
                raise ValidationError(f'{args[1]} - incorrect int number')
        elif isinstance(args[1], int):
            return func(args[0],args[1]) 
        else:
            raise ValidationError(f'{args[1]} - incorrect int number')
    return wrapper


def validation_posit(func):
    @wraps(func)
    def wrapper(*args):
        try: 
            if float(args[1])>=0:
                return func(args[0], (args[1]))
            else:
                raise ValidationError(f'{args[1]} - incorrect positive number')
        except:
            raise ValidationError(f'{args[1]} - incorrect positive number')
    return wrapper


def validation_email(func):
    @wraps(func)
    def wrapper(*args):
        if re.match(r'[A-z0-9\.\+_]+@+(ukr.net|gmail.com)', args[1]):
            return func(*args)
        else:
            raise ValidationError(f'{args[1]} - incorrect payer_email')
    return wrapper


def validation_float(func):
    @wraps(func)
    def wrapper(*args):
        if isinstance(args[1], str):
            x = args[1].replace('.','', 1)
            if  x[1:].isdigit() and (x[0].isdigit() or x[0] == '-' ):
                return func(args[0],float(args[1]))
            else:
                raise ValidationError(f'{args[1]} - incorrect float number')
        elif isinstance(args[1], float):
            return func(args[0],args[1]) 
        else:
            raise ValidationError(f'{args[1]} - incorrect float number')
    return wrapper


def validation_specific_elem(list_):
    def validate(func): 
        @wraps(func) 
        def wrapper(*args):
            if args[1] in list_:
                return func(*args)
            else:
                raise ValidationError(f'{args[1]} - incorrect specific element')
        return wrapper
    return validate


def validation_date(func):
    @wraps(func)
    def wrapper(*args):
        if not args[1] is dt.date.today():
            try:
                return func(*args)
            except:
                raise ValidationError(f'{args[1]} - incorrect date')
    return wrapper
    

def validation_date_after(func):
    @wraps(func)
    def wrapper(*args):
        if dt.datetime.strptime(args[1], '%Y-%m-%d')>args[0]._payment_request_date:
            return func(*args)
        else:
            raise ValidationError(f'due_to_date {args[1]} must be after {args[0]._payment_request_date.date()}')
    return wrapper


def validation_transaction_id(func):
    @wraps(func)
    def wrapper(*args):
        if re.match(r'\d{8}-\d{2}', args[1]) and len(args[1]) == 11:
            return func(*args)
        else:
            raise ValidationError(f'{args[1]} - incorrect transaction id')
    return wrapper

