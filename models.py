from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

Manytomanytable = db.Table('Manytomanytable',
    db.Column('storageitem_id', db.Integer, db.ForeignKey('storageitem.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
)

class StorageItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer, nullable=False)
    stores = db.relationship('Product', secondary=Manytomanytable, backref='storageplace')    
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(64), unique=True, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
