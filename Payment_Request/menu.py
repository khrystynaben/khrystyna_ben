from valid import *
from pr import PaymentRequest

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

    option = menu_option(['','search','add','sort','delete','replace'],5)

    if option =='1':
        text = input('input what you want to search: ')
        cc.search(text)
    elif option=='2':
        new_p_r = PaymentRequest()
        new_p_r.input()
        cc.insert(new_p_r)
        print(cc)
    elif option=='3':
        field_for_sort = input_and_check('input field for sorting: ', [str(item) for item in PaymentRequest.__dict__])
        cc.new_sort(field_for_sort)
        print(cc)
    elif option=='4':
        del_id = input_and_check('input id of element that you want to delete: ',int, positive=True)
        cc.erase(del_id)
        print(cc)
    elif option=='5':
        new_p_r = PaymentRequest()
        new_p_r.input()
        edit_id = input_and_check('input id of element that you want to replace: ',int, positive=True)
        cc.edit(edit_id,new_p_r)
        print(cc)