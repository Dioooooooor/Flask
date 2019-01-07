# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor
    @time: 2018.12.15
    @version: 1.0
    @desc: 商品管理视图
'''

from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

manager_bp = Blueprint("manager", __name__)

@manager_bp.route('/manager')
def managerhome():
    if current_user.is_authenticated:
        return render_template('manager/overview.html')
    return redirect(url_for('login.login'))