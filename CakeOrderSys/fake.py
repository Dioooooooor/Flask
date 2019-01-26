# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor (曹琛)
    @time: 2019.1.7
    @version: 1.0
    @desc: 用于产生测试所需数据
'''

from flask_sqlalchemy import SQLAlchemy
from CakeOrderSys.models import Admin

def fake_createDB():
    SQLAlchemy.create_all()

def fake_admin():
    admin = Admin(
        username='admin'
    )
    admin.set_password("admin")
    SQLAlchemy.session.add(admin)
    SQLAlchemy.session.commit()

if __name__ == "__main__":
    fake_createDB()
    fake_admin()