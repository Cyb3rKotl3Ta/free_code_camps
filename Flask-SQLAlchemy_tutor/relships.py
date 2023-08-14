from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_rel.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db_rel = SQLAlchemy(app)

################## RELATIONSHIPS ##################

class Owner(db_rel.Model):
    id = db_rel.Column(db_rel.Integer, primary_key=True)
    name = db_rel.Column(db_rel.String(20))
    address = db_rel.Column(db_rel.String(100))
    pets = db_rel.relationship('Pet', backref='owner')

class Pet(db_rel.Model):
    id = db_rel.Column(db_rel.Integer, primary_key=True)
    name = db_rel.Column(db_rel.String(20))
    age = db_rel.Column(db_rel.Integer)
    owner_id = db_rel.Column (db_rel.Integer, db_rel.ForeignKey('owner.id'))
