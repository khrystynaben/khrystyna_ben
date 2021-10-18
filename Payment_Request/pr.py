import sys
import datetime as dt
from valid import *


class PaymentRequest:
    def __init__(self, ID = 0, payer_email = None, amount = 0, currency = 'uah',
             payment_request_date = dt.date.today(), payment_due_to_date = dt.date.today(),
             transaction_id ='00000000-00'):
        self._ID = validate_int_and_posit(ID)
        self._payer_email = validate_specific_str(payer_email,'@', ['ukr.net', 'gmail.com'], 2, 1)
        self._amount = validate_float_and_posit(amount)
        self._currency = validate_specific_elem(currency, ['uah', 'usd', 'euro'])
        self._payment_request_date = validate_date(payment_request_date)
        self._payment_due_to_date = validate_date(payment_due_to_date)
        self._transaction_id = validate_str_with_digits(transaction_id, '-', 2)

    def __str__(self):
            return f"{self._ID}, {self._payer_email}, {self._amount}, {self._currency}, " + \
                   f"{self._payment_request_date.strftime('%Y-%m-%d')}, {self._payment_due_to_date.strftime('%Y-%m-%d')}, {self._transaction_id}"


    def set_ID(self, ID):
        self._ID = validate_int_and_posit(ID) 


    def set_payer_email (self, payer_email):
        self._payer_email = validate_specific_str(payer_email,'@', ['ukr.net', 'gmail.com'], 2, -1)


    def set_amount (self, amount):
        self._amount = validate_float_and_posit(amount)


    def set_currency (self, currency):
        self._currency = validate_specific_elem(currency, ['uah', 'usd', 'euro'])


    def set_payment_request_date (self, payment_request_date):
        self._payment_request_date = validate_date(payment_request_date)



    def set_payment_due_to_date(self, payment_request_date):
        self._payment_request_date = validate_date(payment_request_date)


    def set_transaction_id (self, transaction_id):
        self._transaction_id = validate_str_with_digits(transaction_id, '-', 2)

   
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
        self._ID = input('id: ')
        self._payer_email = input('payer email: ')
        self._amount = input('amount: ')
        self._currency = input('currency: ')
        self._payment_request_date =  dt.datetime.strptime(input('p request date: '), '%Y-%m-%d')  
        self._payment_due_to_date = dt.datetime.strptime(input('p due to date: '), '%Y-%m-%d')
        self._transaction_id = input('transaction id: ')







