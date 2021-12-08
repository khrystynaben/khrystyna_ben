from valid import *
from vaccination_p_r import *

def checking_for_menu(x, type_check, positive=False):
    if type_check is int and positive==True:
        return validate_int_and_posit(x)
    elif type_check is int and positive==False:
        return validate_int(x)
    elif type(type_check) is list:
        return validate_specific_elem(x, type_check)
    elif type_check is float:
         return change_to_float(x)


def input_and_check(text, type_check, positive=False):
    temp_var = input(text)
    temp_var = checking_for_menu(temp_var, type_check, positive=False)
    return temp_var

def menu_option(text, kk):
    for i in range (1, kk+1):
        print(f"Input {i} if you want to",text[i])
    input_option = input_and_check( "? ", [str(x) for x in range(1,kk+1)])
    return input_option



def menu(cc):

    option = menu_option(['','print','add','most popular hour','most popular point'],4)

    if option =='1':
        print(cc)
    elif option=='2':
        new_e = VaccinationPointRequest()
        cc.insert(new_e)
    elif option=='3':
        print('all spendings: ')
    elif option=='4':
        cc.popular_point()

 