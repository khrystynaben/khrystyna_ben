import sys
import datetime as dt
from valid import *


class PaymentRequest:
    def __init__(self, ID, payer_email=None, amount=0, currency='uah',
             payment_request_date=dt.datetime.now(), payment_due_to_date=dt.datetime.now(),
             transaction_id='00000000-00'):
        self._ID = self.__validate_id(ID)
        self._payer_email =self.__validate_payer_email(payer_email)
        self._amount = self.__validate_amount(amount)
        self._currency = self.__validate_currency (currency)
        self._payment_request_date = self.__validate_payment_request_date(payment_request_date)
        self._payment_due_to_date = self.__validate_payment_due_to_date(payment_due_to_date)
        self._transaction_id = self.__validate_transaction_id (transaction_id)

    def __str__(self):
            return f" Paym_Request: {self._ID}, {self._payer_email}, {self._amount}, {self._currency}, " + \
                   f"{self._payment_request_date.strftime('%Y/%m/%d')}, {self._payment_due_to_date.strftime('%Y/%m/%d')}, {self._transaction_id}"


    def set_ID(self, ID):
        self._ID = self.__validate_id(ID) 

    @staticmethod
    def __validate_id(ID):
        if isinstance(ID, str):
            ID = change_to_integer(ID)
        if is_positive_integer(ID):
            return ID
        wrong('ID')


    def set_payer_email (self, payer_email):
        self._payer_email = self.__validate_payer_email(payer_email)

    @staticmethod
    def __validate_payer_email(payer_email):
        if payer_email is None:
            return 'no_email'
        temp_var = str(payer_email)
        parts = temp_var.split('@')
        if len(parts) != 2 or parts[-1] not in ['ukr.net','gmail.com']:
            wrong('payer_email')
        return temp_var

    def set_amount (self, amount):
        self._amount = self.__validate_amount(amount)

    @staticmethod
    def __validate_amount(amount): 
        if isinstance(amount, str):
            amount = change_to_float(amount)
        if amount >= 0:
            return amount
        wrong('amount')

    def set_currency (self, currency):
        self._currency = self.__validate_currency(currency)

    @staticmethod
    def __validate_currency(currency):
        if currency in ['uah', 'usd', 'euro']:
            return currency
        wrong('currency')

    def set_payment_request_date (self, payment_request_date):
        self._payment_request_date = self.__validate_payment_request_date(payment_request_date)

    @staticmethod
    def __validate_payment_request_date(payment_request_date):
        return dt_valid(payment_request_date)

    def set_payment_due_to_date(self, payment_request_date):
        self._payment_request_date = self.__validate_payment_due_to_date(payment_request_date)

    @staticmethod
    def __validate_payment_due_to_date(payment_due_to_date):
        return dt_valid(payment_due_to_date)

    def set_transaction_id (self, transaction_id):
        self._transaction_id = self.__validate_transaction_id(transaction_id)

    @staticmethod
    def __validate_transaction_id(transaction_id): 
        parts = str(transaction_id).split('-')
        if len(parts)==2 and len(parts[0])==8 and len(parts[1].strip())==2 and parts[0].isdigit() and parts[1].strip().isdigit():
            return transaction_id
        wrong('transaction_id')

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
        for item in [self._ID, self._payer_email, self._amount, self._currency, 
                    self._payment_request_date,self._payment_due_to_date,self._transaction_id]: 
            if x in str(item):
                return True
        return False


    def input(self):
        self._ID = input('id: ')
        self._payer_email = input('payer email: ')
        self._amount = input('amount: ')
        self._currency = input('currency: ')
        self._payment_request_date = input('p request date: ')
        self._payment_due_to_date = input('p due to date: ')
        self._transaction_id = input('transaction id: ')








