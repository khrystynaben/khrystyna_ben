import datetime as dt
#from valid import*
import time as tm
from my_exception import ValidationError
import re

def validation_int(func):
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
    def wrapper(*args):
        try: 
            if float(args[1])>=0:
                return func(args[0], (args[1]))
            else:
                raise ValidationError(f'{args[1]} - incorrect positive number')
        except:
            raise ValidationError(f'{args[1]} - incorrect positive number')
    return wrapper


def validation_date(func):
    def wrapper(*args):
        if not args[1] is dt.date.today():
            try:
                return func(args[0],dt.datetime.strptime(args[1], '%Y-%m-%d').date())
            except:
                raise ValidationError(f'{args[1]} - incorrect date')
    return wrapper

def validation_time(func):
    def wrapper(*args):
        try:
            #print(args[0])
            x = tm.time.strptime(args[1], '%H:%M')
            #print(x)
            #print(x.time())
            return func(args[0], x.time())
            '''
            if x < tm.time('18:00') and x > tm.time('10:00'):
                return func(args[0], x.time())
            else:
                raise ValidationError(f'{args[1]} - incorrect time1')
                '''
        except:
            raise ValidationError(f'{args[1]} - incorrect time2')
    return wrapper



def validation_name(func):
    def wrapper(*args):
        if args[1].isalpha():
            return func(*args)
        else:
            raise ValidationError(f'{args[1]} - incorrect name')
    return wrapper


def validation_point(func):
    def wrapper(*args):
        if re.match(r'\w', args[1]):
            return func(*args)
        else:
            raise ValidationError(f'{args[1]} - incorrect point')
    return wrapper

def validation_specific_elem(list_):
    def validate(func): 
        def wrapper(*args):
            if args[1] in list_:
                return func(*args)
            else:
                raise ValidationError(f'{args[1]} - incorrect specific element')
        return wrapper
    return validate