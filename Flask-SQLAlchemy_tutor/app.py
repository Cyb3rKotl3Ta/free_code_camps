from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)


################## BASE ##################
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    date_joined = db.Column(db.Date, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<User: {self.name}>'
    
    @classmethod
    def create_user(cls, name, email):
        new_user = cls(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    def change_email(self, new_email):
        self.email = new_email
        db.session.commit()

    def change_username(self, new_username):
        self.name = new_username
        db.session.commit()

# user1 = User.query.filter_by(name='Caroline').first()
# user1.change_username(new_username='Caroline')


