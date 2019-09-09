from os import environ

from flask import Flask
from flask_restful import Api

from applications.db import db
from applications.gamma_api import add_module_gamma

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

api = Api(app)
db.init_app(app)
add_module_gamma(api)

with app.app_context():
    db.create_all()
