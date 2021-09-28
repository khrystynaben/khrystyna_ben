import sys
from os.path import exists
from pr import PaymentRequest
from valid import *

class Collection:
    def __init__(self, file_name):
        self.payments = []
        self.read(file_name)

    def __str__(self):
        s = '' 
        for item in self.payments:
            s += str(item) + '\n' 
        return s
        

    def read(self, file_name):
        if exists(file_name):
            with open(file_name, 'r') as f:
                for i, line in enumerate(f):
                    print(f'reading line {i} ...', end = ' ')
                    row = line.split()
                    item = PaymentRequest(*row)
                    self.payments.append(item)
                    print('done')
        else:
            sys.exit(f'{file_name} does not exists')
    
    def search(self, x):
        print(f'search results for {x}:')
        label = False
        for payment_ in self.payments:
            if payment_.elem_found(x):
                print(payment_)
                label = True
        if label == False:
            print ("no results")

    def sort(self, field):
        if field == 'ID':
            self.payments.sort(key = lambda payment_: payment_._ID)
        elif field == 'payer_email':
            self.payments.sort(key = lambda payment_: payment_._payer_email)
        elif field == 'amount':
            self.payments.sort(key = lambda payment_: payment_._amount)
        elif field == 'currency':
            self.payments.sort(key = lambda payment_: payment_._currency)
        elif field == 'payment_request_date':
            self.payments.sort(key = lambda payment_: payment_._payment_request_date)
        elif field == 'payment_due_to_date':
            self.payments.sort(key = lambda payment_: payment_._payment_due_to_date)
        elif field == 'transaction_id':
            self.payments.sort(key = lambda payment_: payment_._transaction_id)
        else:
            print('Wrong field')
        

    def erase(self, id_):
        for i in range(len(self.payments)):
            if str(self.payments[i].get_ID)== str(id_):
                self.payments.pop(i)
                break
    
    def insert(self,payment_):
        self.payments.append(payment_)

    def edit(self, id_, payment_):
        for i in range(len(self.payments)):
            if str(self.payments[i].get_ID)== str(id_):
                self.payments.pop(i)
                self.payments.append(payment_)
                break

    def menu(self,cc):
        print('input 1 if you want to search something: ')
        print('input 2 if you want to add new element: ')
        print('input 3 if you want to sort elements: ')
        print('input 4 if you want to delete element: ')
        print('input 5 if you want to replace element: ')
        option = input('? ')
        option = valid_specific_elem(option, ['1','2','3','4','5'])
        if option=='1':
            text = input('input what yoy want to search: ')
            cc.search(text)
        elif option=='2':
            new_p_r = PaymentRequest(6723490, 'asdfg@gmail.com', 9000, 'uah', '2000/01/01', '2021/09/29', '89023894-90')
            cc.insert(new_p_r)
            print(cc)
        elif option=='3':
            field_for_sort = input('input field for sorting: ')
            field_for_sort = valid_specific_elem(field_for_sort, ['ID','payer_email', 'amount', 'currency', 
                    'payment_request_date','payment_due_to_date','transaction_id'])
            cc.sort(field_for_sort)
            print(cc)
        elif option=='4':
            del_id = input('input id of element that you want to delete: ')
            del_id = valid_int_posit(del_id)
            cc.erase(del_id)
            print(cc)
        elif option=='5':
            new_p_r = PaymentRequest(6723490, 'asdfg@gmail.com', 9000, 'uah', '2000/01/01', '2021/09/29', '89023894-90')
            edit_id = input('input id of element that you want to replace: ')
            edit_id = valid_int_posit(edit_id) 
            cc.edit(edit_id,new_p_r)
            print(cc)

