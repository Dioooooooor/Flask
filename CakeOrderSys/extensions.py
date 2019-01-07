# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor
    @time: 2018.12.15
    @version: 1.0
    @desc: 扩展插件
'''

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from CakeOrderSys.models import Admin
    user = Admin.query.get(int(user_id))
    return user