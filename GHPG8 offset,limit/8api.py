from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:1234@localhost:5432/payment_request"
#app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['USER']}:{os.environ['PASSWORD']}@{os.environ['HOST']}/{os.environ['DATABASE']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)







