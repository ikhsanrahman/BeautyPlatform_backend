
import datetime
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from app.api.create_app import db 
from app.api.config.config import Config 

TIME = Config.time()

####################################### ADMIN AREA #################################

class Admin(db.Model):
    __tablename__ = "admin"

    id                          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name                        = db.Column(db.String(255), unique=True, default="beauty")
    password                    = db.Column(db.String(255), unique=True)
    password_hash               = db.Column(db.String(255), unique=True)
    login_at                    = db.Column(db.DateTime, default=TIME)
    logout_at                   = db.Column(db.DateTime)

    def __repr__(self):
        return '<this admin is {} >'.format(self.name)

####################################### BUYER AREA #################################

class Buyer(db.Model):
    __tablename__ = 'buyers'
    
    id          	           = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name                  = db.Column(db.String(255))
    email       	           = db.Column(db.String(255), unique=True)
    password    	           = db.Column(db.String(255))
    password_hash              = db.Column(db.String(255))
    gender                     = db.Column(db.String(255))
    phone_number    	       = db.Column(db.String(255))
    address                    = db.Column(db.Text)
    status_buyer               = db.Column(db.Boolean(), default=True)
    created_at  	           = db.Column(db.DateTime, default=TIME)
    updated_at                 = db.Column(db.DateTime, default=TIME)
    deleted_at                 = db.Column(db.DateTime, default=TIME)

    
    def generate_password_hash(self, password) :
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password) :
        return check_password_hash(self.password_hash, password)       

    def set_status_buyer(self, status):
        self.status_buyer = status

    def __repr__(self):
        return '< This buyer is {} >'.format(self.full_name)


class SkinFile(db.Model):
    __tablename__='skin_file'

    id                          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filename                    = db.Column(db.String(255))
    status_file                 = db.Column(db.Boolean, default=True)
    create_at                   = db.Column(db.DateTime, default=TIME)
    updated_at                  = db.Column(db.DateTime)
    deleted_at                  = db.Column(db.DateTime)

    def __repr__(self):
        return '< This info has title {} >'.format(self.filename)


####################################### SELLER AREA #################################

class Seller(db.Model):
    __tablename__ = 'sellers'
    
    id                         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name                  = db.Column(db.String(255))
    email                      = db.Column(db.String(255), unique=True)
    password                   = db.Column(db.String(255))
    password_hash              = db.Column(db.String(255))
    gender                     = db.Column(db.String(255))
    phone_number               = db.Column(db.String(255))               
    status_seller              = db.Column(db.Boolean(), default=True)
    created_at                 = db.Column(db.DateTime, default=TIME)
    updated_at                 = db.Column(db.DateTime, default=TIME)
    deleted_at                 = db.Column(db.DateTime, default=TIME)
    item                       = db.relationship('Item', backref='sellers', lazy=True)
    
    def generate_password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password) :
        return check_password_hash(self.password_hash, password)       

    def set_status_seller(self, status):
        self.status_seller = status

    def __repr__(self):
        return '< This seller is {} >'.format(self.full_name)


class Item(db.Model):
    __tablename__ = 'items'
   
    id                           = db.Column(db.Integer, primary_key=True)
    item_title                   = db.Column(db.String(255))
    status_item                  = db.Column(db.Boolean(), default=True)
    description                  = db.Column(db.Text)
    price                        = db.Column(db.String(255))
    number_like                  = db.Column(db.Integer, default=0)
    number_dislike               = db.Column(db.Integer, default=0)
    created_at                   = db.Column(db.DateTime, default=TIME)
    updated_at                   = db.Column(db.DateTime, default=TIME)
    deleted_at                   = db.Column(db.DateTime, default=TIME)
    seller                       = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=True)
    file_seller                  = db.relationship('FileSeller', backref='items', lazy=True)
        
    def __repr__(self):
        return '< This item  with title {} belongs to {} >'.format(self.item_title, self.owner)


class FileSeller(db.Model):
    __tablename__ = 'file_seller'
    
    id                          = db.Column(db.Integer, primary_key=True)
    file_title                  = db.Column(db.Text())
    file_name                   = db.Column(db.String(255))
    status_file                 = db.Column(db.Boolean(), default=True)
    created_at                  = db.Column(db.DateTime, default=TIME)
    updated_at                  = db.Column(db.DateTime, default=TIME)
    deleted_at                  = db.Column(db.DateTime, default=TIME)
    item                        = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)

    def __repr__(self):
        return '< This file with title {} belongs to {} >'.format(self.file_title, self.owner)



####################################### PAYMENT AREA #################################

class Payment(db.Model):
    __tablename__ = "payment"

    id                             = db.Column(db.Integer, primary_key=True)
    description                    = db.Column(db.Text)
    status_description             = db.Column(db.Boolean(), default=True)
    created_at                     = db.Column(db.DateTime, default=TIME)
    updated_at                     = db.Column(db.DateTime, default=TIME)
    deleted_at                     = db.Column(db.DateTime, default=TIME)
 


