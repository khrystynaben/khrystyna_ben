import sys
from os.path import exists


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

    def insert(self,payment_):
        self.payments.append(payment_)
        self.change_file()


    def edit(self, id_):
        for i in range(len(self.payments)):
            found = False
            if str(self.payments[i].get_ID)== str(id_):
                found = True

                self.payments.pop(i)
                self.payments.append(new_p_r)
                break
        if found == False:
            print("there is not with this id")
        self.change_file()
        

    def get_col_dict(self):
        ll = []
        for item in self.payments[0].__dict__:
            ll.append(str(item))
        return ll


    def append_by_inputting(self, p):
        p.input()
        self.payments.append(p)

