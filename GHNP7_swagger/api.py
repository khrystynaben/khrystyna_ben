from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
import os
#from routes import request_api
from werkzeug.utils import send_from_directory

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:1234@localhost:5432/payment_request"
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['USER']}:{os.environ['PASSWORD']}@{os.environ['HOST']}/{os.environ['DATABASE']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static',path)
    

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

#app.register_blueprint(request_api.get_blueprint())

#app.register_blueprint()




