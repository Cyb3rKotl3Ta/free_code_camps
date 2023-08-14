from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_mtm.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db_mtm = SQLAlchemy(app)


user_channel = db_mtm.Table('user_channel',
                            db_mtm.Column('user_id', db_mtm.Integer, db_mtm.ForeignKey('user.id')),
                            db_mtm.Column('channel_id', db_mtm.Integer, db_mtm.ForeignKey('channel.id'))    
                          )

class User(db_mtm.Model):
    id = db_mtm.Column(db_mtm.Integer, primary_key=True)
    name = db_mtm.Column(db_mtm.String(50))
    following = db_mtm.relationship('Channel', secondary=user_channel, backref='followers')

    def __repr__(self):
        return f'<User: {self.name}>'
    

class Channel(db_mtm.Model):
    id = db_mtm.Column(db_mtm.Integer, primary_key=True)
    name = db_mtm.Column(db_mtm.String(20))

    def __repr__(self):
        return f'<Channel: {self.name}>'