import sys
import datetime as dt
from decorators import *
from valid import *
from my_exceptions import ValidationError


class PaymentRequest:
    def __init__(self, ID = 0, payer_email = 'xxxxxxxx@gmail.com', amount = 0.0, currency = 'uah',
             payment_request_date = '2021-09-16', payment_due_to_date = '2021-10-16',
             transaction_id ='00000000-00'):
        self.set_ID(ID) 
        self.set_payer_email(payer_email)
        self.set_amount(amount)
        self.set_currency(currency)
        self.set_payment_request_date(payment_request_date)
        self.set_payment_due_to_date(payment_due_to_date)
        self.set_transaction_id(transaction_id)

    def __str__(self):
            return f"{self._ID}, {self._payer_email}, {self._amount}, {self._currency}, " + \
                   f"{self._payment_request_date.strftime('%Y-%m-%d')}, {self._payment_due_to_date.strftime('%Y-%m-%d')}, {self._transaction_id}"

    @validation_int
    @validation_posit
    def set_ID(self, ID):
        self._ID = ID

    @validation_email
    def set_payer_email (self, payer_email):
        self._payer_email = payer_email

  
    @validation_float
    @validation_posit
    def set_amount(self, amount):
        self._amount = amount

    @validation_specific_elem(['uah', 'usd', 'euro'])
    def set_currency (self, currency):
        self._currency = currency


    @validation_date
    def set_payment_request_date (self, payment_request_date):
        self._payment_request_date = dt.datetime.strptime(payment_request_date, '%Y-%m-%d')  

    @validation_date_after
    @validation_date
    def set_payment_due_to_date(self, payment_due_to_date):
        self._payment_due_to_date = dt.datetime.strptime(payment_due_to_date, '%Y-%m-%d')  

    @validation_transaction_id
    def set_transaction_id (self, transaction_id):
        self._transaction_id = transaction_id

   
    @property
    def get_ID(self):
        return self._ID

    @property
    def get_payer_email (self):
        return self._payer_email

    @property
    def get_amount (self):
        return self._amount

    @property
    def get_currency (self):
        return self._currency

    @property
    def get_payment_request_date (self):
        return self._payment_request_date

    @property
    def get_payment_due_to_date (self):
        return self._payment_request_date

    @property
    def get_transaction_id (self):
        return self._transaction_id

    def elem_found(self, x):
        for item in self.__dict__.values(): 
            if x in str(item):
                return True
        return False


    def input(self):
        setters = filter(lambda x: x.startswith('set'), list(PaymentRequest.__dict__.keys()))
        for item in setters:
            while True:
                    label = False
                    try:
                        x = getattr(self,item)
                        x(input(f'input {x.__name__[4:] }: '))
                        label = True
                    except ValidationError as error:
                        print(error)
                    if label == True:
                        break
     
        
        
        
             







