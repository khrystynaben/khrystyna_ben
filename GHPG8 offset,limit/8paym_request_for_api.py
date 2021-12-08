from menu import *
#from flask import Flask, jsonify 
from decorators import *
from valid import *
from my_exceptions import ValidationError
#from flask_sqlalchemy import SQLAlchemy 
#from flask_marshmallow import Marshmallow
from api import db,ma

class PaymentRequest (db.Model):
    __tablename__ = "payment_request"
    ID = db.Column(db.Integer, primary_key=True)
    payer_email = db.Column(db.String(50))
    amount = db.Column(db.String(30))
    currency = db.Column(db.String(11))
    payment_request_date = db.Column(db.String(15))
    payment_due_to_date = db.Column(db.String(15))
    transaction_id = db.Column(db.String(15))

    def __init__(self, ID = 0, payer_email = 'xxxxxxxx@gmail.com', amount = '0.0', currency = 'uah',
             payment_request_date = '2021-09-16', payment_due_to_date = '2021-10-16',
             transaction_id ='00000000-00'):
        self.set_ID(ID) 
        self.set_payer_email(payer_email)
        self.set_amount(amount)
        self.set_currency(currency)
        self.set_payment_request_date(payment_request_date)
        self.set_payment_due_to_date(payment_due_to_date)
        self.set_transaction_id(transaction_id)

    def toJson(self):
        return {
            "ID" : str(self.get_ID),
            "payer_email" : str(self.get_payer_email),
            "amount" : str(self.get_amount),
            "currency" : str(self.get_currency),
            "payment_request_date" : self.get_payment_request_date,
            "payment_due_to_date" : self.get_payment_due_to_date,
            "transaction_id": str(self.get_transaction_id)
        }

    def toJson2(self):
        return {
            "ID" : self.ID.value,
            "payer_email" : self.payer_email.value,
            "amount" : self.amount.value,
            "currency" : self.currency.value,
            "payment_request_date" : self.payment_request_date.value,
            "payment_due_to_date" : self.payment_due_to_date.value,
            "transaction_id": self.transaction_id.value
        }
    
    def __str__(self):
            return f"{self.ID}, {self.payer_email}, {self.amount}, {self.currency}, " + \
                   f"{self.payment_request_date}, {self.payment_due_to_date}, {self.transaction_id}"

    @validation_int
    @validation_posit
    def set_ID(self, ID):
        self.ID = ID

    @validation_email
    def set_payer_email (self, payer_email):
        self.payer_email = payer_email

  
    @validation_float
    @validation_posit
    def set_amount(self, amount):
        self.amount = amount

    @validation_specific_elem(['uah', 'usd', 'euro'])
    def set_currency (self, currency):
        self.currency = currency


    #@validation_date
    def set_payment_request_date (self, payment_request_date):
        self.payment_request_date =payment_request_date

    #@validation_date_after
    #@validation_date
    def set_payment_due_to_date(self, payment_due_to_date):
        self.payment_due_to_date = payment_due_to_date

    @validation_transaction_id
    def set_transaction_id (self, transaction_id):
        self.transaction_id = transaction_id

   
    @property
    def get_ID(self):
        return self.ID

    @property
    def get_payer_email (self):
        return self.payer_email

    @property
    def get_amount (self):
        return self.amount

    @property
    def get_currency (self):
        return self.currency

    @property
    def get_payment_request_date (self):
        return self.payment_request_date

    @property
    def get_payment_due_to_date (self):
        return self.payment_due_to_date
    @property
    def get_transaction_id (self):
        return self.transaction_id

    def elem_found(self, x):
        for item in self.__dict__.values(): 
            if x in str(item):
                return True
        return False

    @staticmethod
    def get_attributes():
        attributes = []
        for attr, values in vars(PaymentRequest).items():
            if not attr.startswith("_") and not attr.startswith("set") and not attr.startswith("get") and not attr.startswith("elem") and not attr.startswith("__") and not attr.startswith("to"):
                attributes.append(attr)
        return attributes

    #@staticmethod
    #def list_of_filds():
        #return ['ID', 'payer_email', 'amount', 'currency', 'payment_request_date', 'payment_due_to_date','transaction_id']
'''
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
                        '''
     
# Product Schema 
class PaymRequestSchema(ma.Schema): 
    class Meta: 
        fields = ('ID', 'payer_email', 'amount', 'currency', 'payment_request_date', 'payment_due_to_date', 'transaction_id')
