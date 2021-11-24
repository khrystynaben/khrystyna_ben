from os.path import exists
from caretaker import CareTaker
from collect import Collection
from valid import *
from menu import *
from flask import Flask, jsonify 
from my_exceptions import ValidationError


app = Flask(__name__)
c = Collection('js.json')
print(c)

new_paym =  {
            "ID" : "8695066767",
            "payer_email" : "khryst.rty@gmail.com",
            "amount" : "8900",
            "currency" : "uah",
            "payment_request_date" : "2020-02-15",
            "payment_due_to_date" : "2020-03-07",
            "transaction_id": "14536700-23"
        }


@app.route('/payment/<given_id>/', methods=['DELETE'])
def delete_by_id(given_id):
    if c.erase2(given_id):
        return jsonify({"status": 200, "message": "payment has been successfully deleted"})
    else:
        return jsonify({"status": 404, "message": "payment is not found"})


@app.route('/payment/<given_id>', methods=['GET'])
def get_one(given_id):
    for i in range(len(c.payments)):
            if str(c.payments[i].get_ID)== str(given_id):
                res = c.payments[i].__dict__
            return jsonify(res)
    else:
        return jsonify({"status": 404, "message": "payment is not found"})

@app.route('/payment', methods=['GET'])
def get_all():
    if len(c.payments) > 0:
        for i in range (len(c.payments)):
            return jsonify(c.payments[i].__dict__)
    else:
        return jsonify({"status": 404, "message": "payment is not found"})
    
@app.route('/payment/<given_id>', methods=['PUT'])
def update(given_id):
    if c.edit2(given_id) is False:
        return jsonify({"status": 404, "message": "payment is not found"})
    else:
        for i in range (len(c.payments)):
            return jsonify(c.payments[i].__dict__)


@app.route('/payment', methods=['POST'])
def add():
    try:
        new_paym_for_insert = PaymentRequest(new_paym)
        c.insert(new_paym_for_insert)
        return jsonify({"status": 200, "message": "payment has been successfully added"})
    except ValidationError as error:
        return jsonify({"status": 400, "message": str(error) })




app.run()
'''
c = Collection('js.json')
print(c)

n = input_and_check('number of states: ', int, positive=True)
handler = CareTaker(c, n)

while True:
    menu(c, handler)
    do_next = input("1 - next; 2 - exit\n? ")
    do_next = validate_specific_elem(do_next, ['1', '2'])
    if do_next == '2':
        break
'''

