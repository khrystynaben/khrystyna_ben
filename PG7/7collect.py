import sys
import json
from os.path import exists
from memento import Memento
from my_exceptions import ValidationError
from pr import PaymentRequest
from valid import *
from copy import deepcopy

new_paym =  {
            "ID" : "8695066767",
            "payer_email" : "khryst.rty@gmail.com",
            "amount" : "8900",
            "currency" : "uah",
            "payment_request_date" : "2020-02-15",
            "payment_due_to_date" : "2020-03-07",
            "transaction_id": "14536700-23"
        }
      
class Collection:
    def __init__(self, file_name):
        self.payments = []
        self.read2(file_name)
        self.file_name = file_name

    def __str__(self):
        s = '' 
        for item in self.payments:
            s += str(item) + '\n' 
        return s

        
    def read2(self, file_name):
        if exists(file_name):
            with open(file_name, 'r', encoding = 'utf-8') as f:
                data = json.load(f)
                for i, payment in enumerate(data):
                    print(f'reading line {i} ...', end = ' ')
                    try:
                        item = PaymentRequest(**payment)
                        self.payments.append(item)
                        print('done')
                    except ValidationError as error:
                        print(error)           
        else:
            sys.exit(f'{file_name} does not exists')


    def read(self, file_name):
        if exists(file_name):
            with open(file_name, 'r') as f:
                for i, line in enumerate(f):
                    print(f'reading line {i} ...', end = ' ')
                    row = line.split()
                    try:
                        item = PaymentRequest(*row)
                        self.payments.append(item)
                        print('done')
                    except ValidationError as error:
                        print(error)           
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


    def new_sort(self, field):
        fields = self.payments[0].__dict__
        if field in fields:
            self.payments.sort(key = lambda payment_: getattr(payment_, field))
            self.change_file()
        else:
            print('Wrong field')
        

    def change_file(self):
        with open(self.file_name,'w') as f:
            text = [str(item).replace(',','') for item in self.payments]
            f.write('\n'.join(text))


    def erase(self, id_):
        for i in range(len(self.payments)):
            if str(self.payments[i].get_ID)== str(id_):
                self.payments.pop(i)
                break
        self.change_file()

    def erase2(self, id_):
        label = False
        for i in range(len(self.payments)):
            if str(self.payments[i].get_ID)== str(id_):
                self.payments.pop(i)
                label = True
                break
        #self.change_file()
        return label
        
    
    def insert(self,payment_):
        self.payments.append(payment_)
        self.change_file()


    def edit(self, id_):
        for i in range(len(self.payments)):
            found = False
            if str(self.payments[i].get_ID)== str(id_):
                found = True
                new_p_r = PaymentRequest(777770000000, 'bbbbbbbbbb@gmail.com', 9999.9, 'uah', '2000-01-01', '2021-09-29', '89023894-90')
                #new_p_r = PaymentRequest()
                #new_p_r.input()
                self.payments.pop(i)
                self.payments.append(new_p_r)
                break
        if found == False:
            print("there is not with this id")
        #self.change_file()

    def edit2(self, id_):
        label = False
        for i in range(len(self.payments)):
            found = False
            if str(self.payments[i].get_ID)== str(id_):
                found = True
                #new_p_r = PaymentRequest(777770000000, 'bbbbbbbbbb@gmail.com', 9999.9, 'uah', '2000-01-01', '2021-09-29', '89023894-90')
                #new_p_r = PaymentRequest()
                #new_p_r.input()
                self.payments.pop(i)
                self.payments.append(new_paym)
                label = True
                break
        if found == False:
            print("there is not with this id")
        #self.change_file()
        return label
        

    def get_col_dict(self):
        ll = []
        for item in self.payments[0].__dict__:
            ll.append(str(item))
        return ll


    def append_by_inputting(self, p):
        p.input()
        self.payments.append(p)


    def save(self):
        return Memento(deepcopy(self.payments))


    def restore(self, memento):
        self.payments = memento.get_state
        self.change_file()