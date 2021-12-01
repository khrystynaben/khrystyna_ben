from flask import Flask, jsonify, request
from decorators import *
from valid import *
from my_exceptions import ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from api import db, app
from paym_request_for_api import PaymentRequest, PaymRequestSchema
import os

payment_schema = PaymRequestSchema()
payment_schema = PaymRequestSchema(many=True)

@validation_offset
def conrol_limits(list_of_elem, given_offset, given_limit):
    elem_from = given_offset * given_limit
    elem_to = (given_offset + 1) * given_limit
    if elem_from >= len(list_of_elem):
        return {"status": 404, "message": "payment is not found"}
    if elem_to > len(list_of_elem):
        elem_to = len(list_of_elem)
    to_return = []
    for x in range(elem_from, elem_to):
        to_return.append((list_of_elem[x]))
    return to_return


@app.route('/payments/<given_id>', methods=['DELETE'])
def delete_request(given_id):
    list_elem = PaymentRequest.query
    elem = PaymentRequest.query.get(given_id)
    if elem not in list_elem:
        return jsonify({"status": 404, "message": "payment is not found"})
    else:
        db.session.delete(elem)
        db.session.commit()
        return jsonify({"status": 200, "message": "payment has been successfully deleted"})


@app.route('/payments/', methods=['GET'])
def get_all_with_sort_and_search():
    list_paym = PaymentRequest.query.all()
    print(list_paym)
    if len(list_paym) > 0:
        if 'sort_by' in request.args and 'sort_type' in request.args:
            fields = list_paym[0].__dict__
            field = request.args['sort_by']
            if field in fields:
                list_paym.sort(key=lambda payment_: getattr(payment_, field))
                if request.args['sort_type'] == "desc":
                    list_paym.reverse()
        if 's' in request.args:
            find_part = request.args['s']
            found = []
            for payment_ in list_paym:
                if payment_.elem_found(find_part):
                    found.append(payment_.toJson())
            to_return = found
            #return jsonify(res)
        else:
            res3 = []
            for i in range (len(list_paym)):
                res3.append(list_paym[i].toJson())
            #return jsonify(res3)
            to_return = res3
        if 'limit' in request.args:
            if 'offset' in request.args:
                to_return = conrol_limits(to_return, request.args['offset'], request.args['limit'])
            else:
                to_return = conrol_limits(to_return, 0, request.args['limit'])
        return jsonify(to_return)
    else:
        return jsonify({"status": 404, "message": "payment is not found"})


@app.route('/payments/<given_id>', methods=['GET'])
def get_one_request(given_id):
    list_elem = PaymentRequest.query
    elem = PaymentRequest.query.get(given_id)
    if elem not in list_elem:
        return jsonify({"status": 404, "message": "payment is not found"})
    return jsonify({"status": 200, "message": "Successfully found request"}, {"info":elem.toJson()}), 200


@app.route('/payments/<given_id>', methods=['PUT'])
def update_request(given_id):
    list_elem = PaymentRequest.query
    elem = PaymentRequest.query.get(given_id)
    if elem not in list_elem:
        return jsonify({"status": 404, "message": "payment is not found"})
    else:
        dani = []
        for key in PaymentRequest.get_attributes():
            dani.append(request.json[key])
        try:
            new_payment = PaymentRequest(*dani)
        except ValidationError as error:
            return jsonify({"status": 400, "message": str(error)})
        db.session.delete(elem)
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({"status": 200, "message": "payment has been successfully updated"})


@app.route('/payments', methods=['POST'])
def add_request():
    for elem in PaymentRequest.query:
        if request.json["ID"] == elem.get_ID:
            return jsonify({'status': 404, "message": "payment already exits"})
    dani = []
    for key in PaymentRequest.get_attributes():
        dani.append(request.json[key])
    try:
        new_payment = PaymentRequest(*dani)
        print(new_payment)
    except ValidationError as error:
        return jsonify({"status": 400, "message": str(error)})

    db.session.add(new_payment)
    db.session.commit()
    return jsonify({"status": 200, "message": "payment has been successfully added"})


if __name__ == '__main__':
    app.run(debug=True)