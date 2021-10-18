import sys
from os.path import exists
from pr import PaymentRequest
from valid import *

class Collection:
    def __init__(self, file_name):
        self.payments = []
        self.read(file_name)
        self.file_name = file_name

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
                    try:
                        item = PaymentRequest(*row)
                        self.payments.append(item)
                        print('done')
                    except:
                        pass
                    
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
    
    def insert(self,payment_):
        self.payments.append(payment_)
        self.change_file()

    def edit(self, id_, payment_):
        for i in range(len(self.payments)):
            if str(self.payments[i].get_ID)== str(id_):
                self.payments.edit()
                self.payments.append(payment_)
                break
        

