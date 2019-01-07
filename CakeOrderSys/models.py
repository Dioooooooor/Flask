# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor
    @time: 2018.12.21
    @version: 1.0
    @desc: 数据模型
'''
from flask_login import UserMixin
from CakeOrderSys.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

#商品模型
class Commodity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    price = db.Column(db.Float)
    detail = db.Column(db.Text)

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
