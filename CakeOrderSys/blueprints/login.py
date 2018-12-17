# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor
    @time: 2018.12.15
    @version: 1.0
    @desc: 商品管理视图
'''

from flask import Blueprint
from flask_login import login_user

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'hello world!'

@login_bp.route('/logout')
def logout():
    return 'hello world!'