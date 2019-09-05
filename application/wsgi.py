from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from applications.db import db
from applications.gamma_api import add_module_gamma

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@mysql:3306/dbproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'skjdhgvksdvkghvkhg'
api = Api(app)

db.init_app(app)

migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    pass
    # db.create_all()


add_module_gamma(api)
