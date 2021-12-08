import sys
from os.path import exists
from my_exception import ValidationError
from vaccination_p_r import *
from valid import *

class Collection:
    def __init__(self, file_name):
        self.requests = []
        self.read(file_name)
        self.file_name = file_name

    def __str__(self):
        s = '' 
        for item in self.requests:
            s += str(item) + '\n' 
        return s
        

    def read(self, file_name):
        if exists(file_name):
            with open(file_name, 'r') as f:
                for i, line in enumerate(f):
                    print(f'reading line {i} ...', end = ' ')
                    row = line.split()
                    try:
                        item = VaccinationPointRequest(*row)
                        self.requests.append(item)
                        print('done')
                    except ValidationError as error:
                        print(error)           
        else:
            sys.exit(f'{file_name} does not exists')
    


    def change_file(self):
        with open(self.file_name,'w') as f:
            text = [str(item).replace(',','') for item in self.requests]
            f.write('\n'.join(text))

    
    def insert(self,v_p_request_):
        self.requests.append(v_p_request_)
        self.change_file()


    def popular_point(self):
        k = [1 for x in range(0,len(self.requests))]
        for i in (0,len(self.requests)):
            print(i)
            for j in (i, len(self.requests),1):
                print(j)
                if self.requests[i].point ==  self.requests[j].point:
                    k[i] +=1

        m = max(k)
        self.requests[m].write_into_file()
                